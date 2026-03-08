class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print("That bird is flying in the sky!")
class RobotBird(Bird):
    def __init__ (self, name, battery=100):
        self.name = name
        self.battery = battery
    def show_battery(self):
        if self.battery <= 0:
            print("Warning: Battery is empty! Please recharge.")
            self.battery = 0
        elif self.battery < 20:
            print("Warning: Battery is low! Consider recharging soon.")
        elif self.battery >= 100:
            self.battery = 100
            print("Whoo! Your bird is fully charged! 🔋")
        else:
            print("Your robot bird has", self.battery, "% battery!")

    def fly(self):
        if self.battery<=15:
            print("Battery too low to fly! Please recharge.")
        else:
            self.battery -= 15
            print("Your robot bird is flying! It's slightly more tired now.")
    def recharge(self):
        self.battery += 50
        if self.battery >= 100:
            self.battery = 100
            print("Whoo! Your bird is fully charged! 🔋")
        elif self.battery <= 0:
            self.battery = 50
            print("Your bird was completely out of battery! It got 50% energy.")
        else:
            print("Whoo! That's 50% more energy!")
MyBird = RobotBird("Nyx")
MyBird.show_battery()
MyBird.fly()
MyBird.show_battery()
MyBird.recharge()
MyBird.fly()
MyBird.fly()
MyBird.show_battery()
MyBird.recharge()
