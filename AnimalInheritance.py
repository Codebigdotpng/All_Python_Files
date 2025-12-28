class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name + " makes a sound!")

class Bird(Animal):
    def fly(self):  # lowercase 'f' (Python style)
        print("That bird is flying in the sky!")

class Parrot(Bird):
    def copy(self):  # lowercase 'c'
        speech = input("Try to say something!: ")
        print(self.name, "can copy your words! Look.", self.name, "says it!")
        print(self.name, "says:", speech)
    def speak(self):
        print(self.name, "says: Hello! I'm a talking parrot! 🦜")

# --- Robot Dog ---
class RoboDog(Animal):
    def __init__(self, name, power, battery=100):
        super().__init__(name)
        self.battery = battery
        self.power = power

    def show_battery(self):
        print("Your robot dog has", self.battery, "% battery!")

    def play(self):
        self.battery -= 20
        if self.battery < 0:
            self.battery = 0
        print("Your robot dog played for a while! It's a bit more tired now.")

    def recharge(self):
        self.battery += 50
        if self.battery > 100:
            self.battery = 100
            print("Whoo! Your pet is fully charged! 🔋")
        else:
            print("Whoo! That's 50% more energy!")

    def protect(self):
        self.battery -= 5
        print("Someone attacked you—but your pet stopped it with", self.power + "! 💥")

# Test everything!
print("=== PARROT ===")
Pet = Parrot("Polly")
Pet.copy()
Pet.speak()
Pet.fly()

print("\n=== ROBO DOG ===")
MyPet = RoboDog("Danny", "SuperBite")
MyPet.protect()
MyPet.show_battery()
MyPet.play()
MyPet.show_battery()
MyPet.recharge()
MyPet.show_battery()