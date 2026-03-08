class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + " makes a sound!")
        
class Bird(Animal):
    def Fly(self):
        print("That bird is flying in the sky!")
        
class Parrot(Bird):
    def copy(self):
        Speech= str(input("Try to say something!:"))
        print(self.name, "can copy your words! Look.",self.name,"Say it!")
        print(self.name, "says-", Speech)
    def speak(self):
        print(self.name, "says- Hello! I'm",self.name)
Pet= Parrot("Polly")
Pet.copy()
Pet.speak()
Pet.Fly()

class RobotParrot(Parrot):
    def __init__ (self, name, power, battery=100):
        super().__init__(name)
        self.battery = battery
        self.power = power
    def copy(self):
        print(self.name, "is a robot parrot but, they can still copy words like a normal parrot.")
        print(self.name, "says-, Hi! I'm a robot parrot! My name is", self.name)
        Speech= str(input("Try to say something!:"))
        super().copy()
    def show_battery(self):
        print("Your robot parrot has", self.battery, "% battery!")
    def fly(self):
        if self.battery<=15:
            print("Battery too low to fly! Please recharge.")
        else:
            self.battery -= 15
            print("Your robot parrot is flying! It's slightly more tired now.")
    def recharge(self):
        self.battery += 50
        if self.battery >= 100:
            self.battery = 100
            print("Whoo! Your parrot is fully charged! 🔋")
        elif self.battery <= 0:
            self.battery = 50
            print("Your parrot was completely out of battery! It got 50% energy.")
        else:
            print("Whoo! That's 50% more energy!")
    def use_power(self):
        print("Your robot parrot used its special power:", self.power + "!")
MyRobotParrot= RobotParrot("RoboPolly", "talon laser")
MyRobotParrot.copy()
MyRobotParrot.speak()
MyRobotParrot.Fly()