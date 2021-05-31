class car():
    """Standart car \n
    varibles: \n
    model = Model of the car \n
    year = what year was the car manufactured\n
    price = cost of the car in kr (Dk kroner)\n
    HK = horsepower 1 = 745.699872 watts \n
    top_speed = top speed in km/t (kilomenters pr hour) \n
    fuel_type = can be petrol, dissel or electric \n
    carring_capacity = max carring weigth in kg (kilo) \n
    weight = cars weigth in kg (kilo) \n
    Geartype = automatick or manuel \n
    doors = amount of intrence points (trunk included) 
    """
    
    def __init__(self, model, mileage, year,price, HK, top_speed, fuel_type,carring_capacity,weight,Geartype,doors):
        """ intializing car"""
        self.model = model
        self.mileage = mileage
        self.year = year
        self.price = price
        self.HK = HK 
        self.top_speed = top_speed
        self.fuel_type = fuel_type
        self.carring_capacity = carring_capacity
        self.weight = weight
        self.Geartype = Geartype
        self.doors = doors

    def repr(self):
        return 'car(r%, r%, r%, r% , r% , r% , r% , r% , r% , r% , r%)' %(self.model, self.mileage, self.year, self.price, self.HK, self.top_speed, 
        self.fuel_type, self.carring_capacity, self.weight, self.Geartype, self.doors)

    def __str__(self):
        return 'model: {model}, mileage: {mileage}, year: {year}, cost: {price}, horsepower: {HK}, topspeed: {top_speed}, fuel_type: {fuel_type}, carring_capcity: {carring_capacity}, weight: {weight}, Geartype: {Geartype}, doors: {doors}.'.format(
            model=self.model, mileage=self.mileage, year=self.year, price=self.price,HK=self.HK,top_speed=self.top_speed,fuel_type=self.fuel_type,carring_capacity=self.carring_capacity,weight=self.weight,Geartype=self.Geartype,doors=self.doors)
#test
#test_car = car("BMW",12000, "2004", 75000, 120, "200 km/t", "benzin", "500 kg" , "950 kg", "manuel", 5 )
#print (test_car)