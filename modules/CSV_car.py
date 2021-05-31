import csv
from os import write
import datetime # used when writing csv


def write_cars_to_CSV(dic_list, filename = "cars.csv"):
    # add all dic of cars to a list (use code eksample i oneNote for csv w inspration )
    model_label = 'model'
    price_label = 'price'
    mileage_label = 'Kilometer'
    year_label = 'Årgang'
    HK_label = 'Hestekræfter'
    Km_L = "Km/l"
    top_speed_label = 'Tophastighed'
    fuel_type_label = 'Brændstoftype'
    carring_capacity_label = 'Max. påhæng'
    weight_label = 'Vægt' 
    Geartype_label = 'Gearkasse'
    doors_label = 'Antal døre'
    csv_headers = [model_label, price_label, mileage_label,year_label,HK_label,Km_L,top_speed_label,fuel_type_label,carring_capacity_label,weight_label,Geartype_label,doors_label]
    
    #print (csv_headers)
   
    with open(filename, 'w', encoding='UTF8', newline="") as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=csv_headers)
        writer.writeheader()
        for car in dic_list:
            writer.writerow(car)
       
def create_filename(cartype):
    my_datetime = datetime.datetime.now()
    date = my_datetime.strftime("%B %d, %Y")
    #optional (write_cars_to_CSV has defualt file_name = cars.csv)
    file_name = str(cartype)+ " " + str(date)+ '.csv' 
    return file_name

def open_csv(file):
    with open(file) as file_obj:
        lines = file_obj.readlines()
        for line in lines:
            print(line.rstrip())

if __name__ == '__main__':
    #list_dic = []
    #list_dic.append({'model': 'Alfa Romeo Giulietta 1,4 Turbo 120 Distinctive', 'price': '104.900 kr.', 'Kilometer': '74.000', 'Årgang': '2011', 'Hestekræfter': '120', 'Km/l': '15,6', 'Tophastighed': '195', 'Brændstoftype': 'Benzin', 'Max. påhæng': '1.300', 'Vægt': '1.255', 'Gearkasse': 'Manue', 'Antal døre': '5'})
    #print (list_dic) #(done)
    #write_cars_to_CSV(list_dic) #(done)
    print(create_filename('alfa')) #(done)
