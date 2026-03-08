class Animal:
    def __init__ (self, species, sound):
        self.species = species
        self.sound = sound
    def speak(self):
        print("The " + self.species + " goes '" + self.sound + "'!")
    def morning_call(self):
        for i in range(3):
            self.speak()       
class Cow(Animal):
    def __init__ (self, name, sound="Moo"):
        self.name = name
        self.sound= sound
    def speak(self):
        print(self.name + " says '" + self.sound + "'!")
MyCow = Cow("Wilbur")
MyCow.speak()
class Pig(Animal):
    def __init__ (self, name, sound="Oink"):
        self.name = name
        self.sound = sound
    def speak(self):
        print(self.name + " says '" + self.sound + "'!")
MyPig = Pig("Porker")
MyPig.speak()
class Chicken(Animal):
    def __init__ (self, name, sound="Cluck"):
        self.name = name
        self.sound = sound
    def speak(self):
        print(self.name + " says '" + self.sound + "'!")
MyChicken = Chicken("Dr. Doodledoo")
MyChicken.speak()
MyCow.morning_call()