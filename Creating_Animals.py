class Animal:
    def __init__ (self, species, sound):
        self.species = species
        self.sound = sound
    def make_sound(self):
        print("The " + self.species + " goes '" + self.sound + "'!")    

Lion = Animal("Lion", "Roar")
Lion.make_sound()
Duck = Animal("Duck", "Quack")
Duck.make_sound()