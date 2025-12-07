import random

class Pet:
    def __init__(self, name, age, species, energy_level):
        self.name = name
        self.age = age
        self.species = species        # safer than using 'type'
        self.energy_level = energy_level

    def play(self):
        if self.energy_level <= 0:
            print(f"{self.name} is too tired to play! 😴")
            return
        print("Let's Start Playing! 🎾")
        energy_used = random.randint(5, 20)
        self.energy_level -= energy_used
        if self.energy_level < 0:
            self.energy_level = 0
        print(f"{self.name} the {self.species} (age {self.age}) used {energy_used} energy!")

    def rest(self):
        print(f"{self.name} is resting... 😌")
        energy_restored = random.randint(10, 30)
        self.energy_level += energy_restored
        print(f"{self.name} regained {energy_restored} energy!")

    def status(self):
        print(f"{self.name} the {self.species} (age {self.age}) has {self.energy_level} energy.")

# Test it!
my_pet = Pet("Rex", 3, "Iguana", 100)
my_pet.status()
my_pet.play()
my_pet.status()
my_pet.rest()
my_pet.status()