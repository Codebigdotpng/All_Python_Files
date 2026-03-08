class SuperAnimal:
    def __init__ (self, name, species, superpower):
        self.name = name
        self.species = species
        self.superpower = superpower
    def power_usage(self):
        print(self.name, "the", self.species, "used", self.superpower + "!")
Mythical_Pet1= SuperAnimal("Shadow", "Cat", "Night Vision")
Mythical_Pet1.power_usage()