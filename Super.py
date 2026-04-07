'''
The super() keyword in Python is used to call methods from a parent (super) class inside a child (subclass).
🔹 Why use super()?
To reuse parent class code
To avoid rewriting methods
To support inheritance properly

'''


#initialise a parent class as Employee-constructor with parameter name, 
# child class as Developer - constructor with parameter prog_lang, user super()

class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, prog_lang):
        super().__init__(name)  
        self.prog_lang = prog_lang
dev1 = Developer("Vinaya", "Python")
print("Name:", dev1.name)
print("Programming Language:", dev1.prog_lang)

 # make a class animal - contain a method with print("animal is shouting"), 
# make 2 child classes #dog - method with print "bow"& cat - method with print "meow"
class Animal:
    def sound(self):
        print("Animal is shouting")
class Dog(Animal):
    def sound(self):
        print("Bow")
class Cat(Animal):
    def sound(self):
        print("Meow")
d = Dog()
c = Cat()
d.sound()
c.sound()