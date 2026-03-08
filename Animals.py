class Animal:
    def __init__ (self, name):
        self.name = name
    def speak(self):
        print(self.name + " makes a sound!")
class Dog(Animal):
    def __init__ (self, name):
        super().__init__(name)
    def speak(self):
        print(self.name, "barks- Woof!")
class Bird(Animal):
    def fly(self):
        print("That bird is flying high!")

bird= Bird("Tweety")
bird.speak()
bird.fly()

class Robot:
    def __init__ (self, name, battery=100):
        self.name = name
        self.battery = battery
    
    def recharge(self):
        self.battery += 50
        if self.battery >= 100:
            self.battery = 100
            print("Whoo! Your robot is fully charged! 🔋")
        elif self.battery <= 0:
            self.battery = 50
            print("Your robot was completely out of battery! It got 50% energy.")
        else:
            print("Whoo! That's 50% more energy!")
class RoboDog(Dog, Robot):
    def __init__ (self, name):
        Dog.__init__(self, name)
        Robot.__init__(self, name)
    def fetch(self):
        if self.battery < 20:
            print("Battery too low to fetch! Please recharge.")
        else:
            self.battery -= 15
            print("Your robot dog fetched the ball!")
            print("It's slightly more tired now.")
            
        
        
    