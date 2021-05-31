import custom_exceptions as my_except
import re # cleaning data

labels= ['Kilometer:','Årgang:', 'Hestekræfter:', 'Km/l:', 'Tophastighed:','Brændstoftype:','Max. påhæng:', 'Vægt:', 'Gearkasse:', 'Antal døre:']
labes_mec = [str(lab).strip(":") for lab in labels]

def find_specific_spec_value(label, specs):
    """ find value in list of specifications (Dou to multiple no named class specifications) \n
    attributs: \n
    label = what label to look for in specs\n
    specs = list of div classes with no name

     """
    for spec in specs:
        if spec.find('span', class_="text-gray-500") is not None:
            if spec.find('span', class_="text-gray-500").text == str(label):
                spec_value = spec.find('span', class_="float-right font-semibold").text
                return spec_value
        elif spec.find('span', class_="spec-label") is not None:
            #print("i at the door with: " + str(label))
            if spec.find('span', class_="spec-label").text == str(label):
                #print ("i got in")
                spec_value = spec.find('span', class_="spec-value").text
                return spec_value
    

def car_specifications(content):
    """ returns dictionariy with car specifikations \n
    content = Html/soup, 
    """
    
    label_type = []
    #try:
    
    if content.find('div', class_="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-y-1 gap-x-14 mt-3 text-sm") is not None:
        label_type = labes_mec
        spec = content.find('div', class_="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-y-1 gap-x-14 mt-3 text-sm")
        specs = spec.findAll(attrs={'class': None})
    elif content.find('div', class_="spec-container") is not None:
        label_type = labels
        spec = content.find('div', class_="spec-container")
        specs = spec.findAll('div', class_="col-xs-4")
    else:
        empt_spec_dic = {}
        for label in labes_mec:
            empt_spec_dic [str(label)] = None
        return empt_spec_dic 
    if  content.find('h1', class_="text-3xl font-bold") is not None:
        model = content.find('h1', class_="text-3xl font-bold").text.strip()
    elif  content.find('div', class_="col-xs-8") is not None:
        model = content.find('div', class_="col-xs-8").text.strip()
    if  content.find('div', class_="flex-1 font-bold text-2xl text-right whitespace-nowrap") is not None:
        getprice = content.find('div', class_="flex-1 font-bold text-2xl text-right whitespace-nowrap").text.strip()
        price = " ".join(re.findall(r'\d+', getprice))
    elif content.find('div', class_="price") is not None:
        price = content.find('div', class_="price").text.strip()
        price = price.replace(".", "")
    
    #except Exception:
     #   raise my_except.new_spec_found("New spec found in: " + str(car_type))
    
    spec_dic= {'model': model, 'price': price}
    
    for label in label_type:    
        try:
            spec_dic [str(label)] = find_specific_spec_value(str(label), specs)
        except Exception as e:
                print (e)
    return spec_dic
    """
        for name,value in zip(specs_name,specs_value) :
            spec_dic[name.text]=value.text
    #except Exception:
     #   pass
    return spec_dic       
    """

if __name__ == '__main__':
    print (labes_mec)
    
 
     