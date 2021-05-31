import bs4 as bs
from matplotlib.pyplot import clabel # beutifulsoup
import requests as rq # get data from url
import datetime # used for speedtest
import car_specefication as cs # custum moduel to help find specifications
import custom_exceptions as my_except # custum moduel with custum a exception
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor



base_url = 'https://bilhandel.dk' # base url

def get_all_cars(car_type, electric = 'no'):
    """Collet all car information, returns list of dictionaris that containing cars\n
    variabel:\n
    car_typ  = name of cartype (BMW etc)\n
    electric = option to inclued electric cars defualt => no
    """
    url = 'https://bilhandel.dk/brugte-biler/'+ str(car_type).lower()
    # get all url to pages containg cars
    all_car_pages= Allpages(url)
    # get all soups from the pages
    all_soups = []
    for car_page in all_car_pages:
        #print ("car page = " + str(car_page))
        all_soups.append(getdata(str(car_page)))
    # get all url to the cars from all the soups    
    all_links_to_car = []
    for soup in all_soups: 
        list_of_links = getcarContent(soup)
        for car_url in list_of_links:
            all_links_to_car.append(car_url)

    # get sepcifications for cars (Nesting a list of dictionaries)
    list_of_specs = []
    for carspec in all_links_to_car:
        list_of_specs.append(getspecifcations(carspec, electric))

    return list_of_specs

def getdata(url):
    r = rq.get(url)
    r.raise_for_status()
    soup = bs.BeautifulSoup(r.text, 'html.parser')
    return soup

def getnextpage(soup):
    page = soup.find('ul', {'class': "pagination"})
    if not page.find('a', {'span': 'næste'}):
        all_ref_links = [a['href'] for a in page.find_all('a', href=True) if a.text]
        ref_link = all_ref_links[-1] 
        next_url = base_url + str(ref_link)
        # guard against base_url 
        if next_url == base_url:
            return None
        else: 
            return next_url
    else:
         return None

def Allpages(url):
    """ returns all url to all the page with cars """
    page_links= [url]
    while True:
        soup = getdata(url)
        url = getnextpage(soup)
        if not url:
            break
        page_links.append(url)
    return page_links

def getcarContent(soup):
    """ returns a list with all url to the cars on a page/soup"""

    content= soup.findAll('div', class_='srp-body')
    car_links = []
    for body in content:
        car_to_add = str(set([a['href'] for a in body.findAll('a', href=True) if a.text]))
        url_to_car = (str(base_url) + str(car_to_add).strip("{}'"))
        car_links.append(url_to_car)
    # last link is allwas some insureces firm    
    car_links.pop()
    return car_links
    
def getspecifcations(url, electric):
    """ Taks a car url and find specefications returns a dictionary\n
    url = url\n
    electric = if electric cars is needed 
    """
    content = getdata(url)
    try:         
        specf_dic = cs.car_specifications(content)
        result = cleandata(specf_dic, electric)
        return result
    except Exception as e :
        raise my_except.new_spec_found(e)
    
def find_specific_spec_value(label, specs):
    """ find value in list of specifications (Dou to multiple no named class specifications) \n
    attributs: \n
    label = what label to look for in specs\n
    specs = list of div classes with no name
     """
    for spec in specs:
        if spec.find('span', class_="spec-label").text == str(label):
            spec_value = spec.find('span', class_="spec-value").text
             
            return spec_value

def multithreading(func, args, workers=5):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)

def cleandata(dic, electric ="no"):
    """Returns dic with no unwanted char, \n
    variabels: \n
    dic = dictionarie elmt to clean \n
    electric = any value but 'no' vil return electric cars """
    
    clean_dic={} 
    # need to strip some chars    
    clean_dic = {k.strip(":"):v.strip('km/t kr. kg km/l') for (k,v) in dic.items() if v is not None}

    
    if 'price' in clean_dic.keys():
        #clean_dic['price'] = str(clean_dic['price']).strip()
        if clean_dic["price"] is not None:
            fix_price = str(clean_dic["price"]).replace(" ","")
            clean_dic['price'] = (str(fix_price).replace('.',''))
            if not str(clean_dic['price']).isdigit():
                clean_dic['price'] = None
    
    if 'Km/l' in clean_dic.keys():  
        if clean_dic['Km/l'] is not None:
            fix_dot = float(str(clean_dic['Km/l']).replace(",","."))
            clean_dic['Km/l'] = round(fix_dot)    
    
    if 'Kilometer' in clean_dic.keys():  
        if clean_dic['Kilometer'] is not None:
            #if len(clean_dic['Kilometer']) <  : 
            fix_dot = float(str(clean_dic['Kilometer']).replace(".",""))
            clean_dic['Kilometer'] = round(fix_dot)    
            # some times mistacks are made try (https://bilhandel.dk/citroen-c4-cactus-12-pt-110-feel/id-938981)
        if  len(str(clean_dic['Kilometer'])) > 7:
            clean_dic['Kilometer'] = None # data can not acount for estimating single cases (can't impute values)
    
    #"""  
     # dou to low results in data only petrol and Diesel is allowed defualt 
    if 'no' in electric:
        if 'Brændstoftype' in clean_dic.keys():
            other = 'other' #  electric
            elm = clean_dic['Brændstoftype']
            if  elm is not None:
                if 'Diesel/E' in elm:
                    clean_dic['Brændstoftype'] = other #'Diesel/E'
                if 'Benzin/E' in elm:
                    clean_dic['Brændstoftype'] = other #'Benzin/E'
                if  elm == 'E':
                    clean_dic['Brændstoftype'] = other #'E'
                if  elm == 'Hybrid':
                    clean_dic['Brændstoftype'] = other #'Hybrid'
    # """

    return clean_dic


#testing method:
#speed test: without multithreading alfa-romeo =  0:00:42.566452
if __name__ == '__main__':
    #viable
    specf_url = 'https://bilhandel.dk/alfa-romeo-giulietta-14-turbo-120-distinctive/id-995760'
    #spec_url_cleantest = 'https://bilhandel.dk/alfa-romeo-giulietta-14-tct-sportiva/id-1003918'
    Alfa_test_link = "https://bilhandel.dk/alfa-romeo-giulietta-14-m-air-150-sprint/id-1004212"
    mercedes_page = 'https://bilhandel.dk/brugte-biler/Mercedes'
    mercedes_url = 'https://bilhandel.dk/lead/mercedes-a250-e-13-amg-line-aut/id-1006415'
    mercedes_url_other_kind = 'https://bilhandel.dk/mercedes-b250-e-13-amg-line-aut/id-984279'
    mercedes_price_fix = 'https://bilhandel.dk/lead/mercedes-b180-18-cdi-be/id-1002799'
    mercedes_el = 'https://bilhandel.dk/mercedes-c300-h-22-hybrid-amg-line-pack/id-952676'
    ford_url = 'https://bilhandel.dk/ford-s-max-ford-s-max-20-ecoblue-st-line-190hk-8g-aut/id-985368'
    #test_soup = getdata(mercedes_page)
    dic = {'distance': '123 km/t', 'price': '200.000', 'vægt': '30 kg', "gearkass":"Manual", "brændstof":"benzin"}
    start = datetime.datetime.now()
    url_car_page1 = 'https://bilhandel.dk/brugte-biler/alfa-romeo'
    #print (multithreading (get_all_cars, url_car_page1))
    #print(get_all_cars("alfa-romeo")[0:5])
    #print(get_all_cars("alfa-romeo")[0])
    #cv.write_cars_to_CSV(get_all_cars(merc), "test_cars.csv")
    #print(getspecifcations('https://bilhandel.dk/citroen-c4-cactus-12-pt-110-feel/id-938981'))
    print(getspecifcations('https://bilhandel.dk/lead/mercedes-a250-e-13-amg-line-aut/id-1006415', 'yes' ))
    print(getspecifcations(Alfa_test_link, 'yes' ))
    finish = datetime.datetime.now() - start
    print (finish)
