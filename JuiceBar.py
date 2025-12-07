class Juice:
    def __init__(self, flavor, size, ice_cubes):
        self.flavor = flavor
        self.size = size
        self.ice_cubes = ice_cubes

    # Now these methods are OUTSIDE __init__ (same indent level!)
    def describe(self):
        print("You have a", self.size, self.flavor, "juice with", self.ice_cubes, "ice cubes.")

    def add_ice(self, cubes):  # ← added 'self', and use 'cubes'
        self.ice_cubes += cubes
        print("Added", cubes, "ice cubes. Total now:", self.ice_cubes)

    def remove_ice(self, amount):  # ← renamed to 'drink' (as in challenge), and added 'self'
        self.ice_cubes -= amount
        if self.ice_cubes < 0:
            self.ice_cubes = 0
        print("Removed", amount, "ice cubes. Total now:", self.ice_cubes)

# Test it
my_order = Juice("Mango", "Large", 5)
my_order.describe()
my_order.add_ice(3)
my_order.remove_ice(6)