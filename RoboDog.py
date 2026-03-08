class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + " makes a sound!")
class RoboDog(Animal):
    def __init__(self, name, power, battery=100):  # ✅ name and power first!
        super().__init__(name)  # 👈 This calls Animal's __init__ (so name is set properly!)
        self.battery = battery
        self.power = power

    def show_battery(self):  # ✅ added (self)
        print("Your robot dog has", self.battery, "% battery!")

    def play(self):  # ✅
        self.battery -= 20
        if self.battery < 0:
            self.battery = 0
        print("Your robot dog played for a while! It's a bit more tired now.")

    def recharge(self):  # ✅
        self.battery += 50
        if self.battery > 100:
            self.battery = 100
            print("Whoo! Your pet is ready to go and fully charged up!")
        print("Whoo! That's 50% more energy!")

    def protect(self):  # ✅
        print("Someone attacked you—but your pet stopped it with", self.power + "! 💥")


# Create your robot dog
MyPet = RoboDog("Danny", "SuperBite")

# Test it!
MyPet.protect()        # ✅ with ()
MyPet.show_battery()
MyPet.play()
MyPet.show_battery()
MyPet.recharge()
MyPet.show_battery()
#Cool!
        