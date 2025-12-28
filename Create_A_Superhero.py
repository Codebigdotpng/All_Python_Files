class Superhero:
    def __init__(self, name, superpower):
        self.name = name
        self.superpower = superpower
    def use_power(self):
        print(self.name + " uses their superpower: " + self.superpower + "!")   
Hero1 = Superhero("Cloaked", "Invisibility")
Hero1.use_power()
