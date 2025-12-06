class Myself:
    def __init__ (self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

Person1= Myself("Karan", 9, "India")
print("Hi! I'm", Person1.name + ". I'm", Person1.age, "years old and I live in", Person1.country + ".")