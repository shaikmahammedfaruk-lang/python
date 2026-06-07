class Bike:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def descripition(self):
        print(f"{self.model}, {self.year},{ self.make}")
b1=Bike("Yamaha Motor Company","Yamaha R15 V4",2008) 
b2=Bike("Honda","Honda Grom",2014)
b1.descripition()  
b2.descripition()