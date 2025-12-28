class Dog:
    def __init__ (self, name, age):
        self.name= name
        self.age= age
    def bark(self):
        print("Woof! My name is " + self.name)
    def introduce(self):
        print("Hello, I am " + self.name + " and I am " , str(self.age) , " years old.")
My_Dog= Dog("Luna", 3)
My_Dog.introduce()

class Cat:
    def __init__ (self, name, favorite_toy):
        self.name= name
        self.favorite_toy= favorite_toy
    def play(self):
        print(self.name + " is playing with " + self.favorite_toy, ", their favorite!")
My_Cat= Cat("Whiskers", "Yarn Ball")
My_Cat.play()