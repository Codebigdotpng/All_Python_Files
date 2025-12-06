class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is",self.name,"and i'm ",self.age,"years old.")

p1 = Person("Karan", 9)
p1.greet()
