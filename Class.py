class Karan:
    def __init__ (me, myname, myage): 
        me.myname= myname
        me.myage= myage

MyObject= Karan("Karan", 9)

print("Hi! I'm", MyObject.myname)
print("I'm", MyObject.myage, "years old.")

class Cat:
    def __init__ (self, name):
        self.name = name
    def meow(self):
        print("Meow! I'm", self.name)

mycat= Cat("Whiskers")

mycat.meow()