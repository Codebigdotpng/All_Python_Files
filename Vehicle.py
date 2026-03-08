class Vehicle:
    def __init__ (self, brand):
        self.brand = brand
    def start(self):
        print("This", self.brand, "vehicle is starting!")
class Car(Vehicle):
    def __init__ (self, brand, model):
        super().__init__(brand)
        self.model = model
    def start(self):
        print("The", self.brand, self.model, "is ready to drive!")
my_car = Car("Toyota", "Camry")
my_car.start()
class ElectricCar(Car):
    def __init__ (self, brand, model, battery=100):
        super().__init__(brand, model)
        self.battery = battery
    def start(self):
        print(self.brand, self.model, "runs silently on electric power!")
    def charge(self):
        self.battery = 100
        print("The", self.brand, self.model, "is now fully charged!")
    def drive(self):
        if self.battery <= 10:
            print("Battery very low! Please charge the car.")
        elif self.battery <= 20:
            print("Battery low! Please charge the car.")
        elif self.battery >=100:
            self.battery = 100
        else:
            self.battery -= 20
            print("The", self.brand, self.model, "is driving! Battery at", self.battery, "%.")