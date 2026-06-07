class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class ElectricCar(Car):
    def refuel(self):
        print("Electric cars do not use fuel")

    def recharge(self):
        print("Battery is charging")
tesla = ElectricCar()

tesla.start()     
tesla.drive()    
tesla.refuel()    
tesla.recharge()          