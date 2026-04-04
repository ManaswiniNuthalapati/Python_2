'''
Python OOPS
🔹 1. Python Classes & Objects
Python is an object-oriented language.
Almost everything is an object (with properties + methods).
A class is a blueprint for creating objects.
Example:
class MyClass:
    x = 5
    
Create Object:
p1 = MyClass()
print(p1.x)
Object = instance of class

🔹 2. init() Method (Constructor)
Every class has a built-in method called __init__().
It runs automatically when an object is created.
Used to assign values (properties) to objects
Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 25)
print(p1.name)
print(p1.age)
Without __init__(), you must assign values manually

🔹 3. self Parameter
self refers to the current object (instance).
Used to access variables and methods inside class
Must be the first parameter in methods
Example:
class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)
self.name means: value belongs to that object

Important:
Name doesn’t have to be self, but we always use it (convention)

🔹 4. Properties (Variables in Class)
Instance Properties
Defined inside __init__()
Belong to each object separately
self.name = name

 Class Properties
Defined outside methods
Shared by all objects
class Person:
    species = "Human"   # class property
Example:
class Person:
    species = "Human"
    def __init__(self, name):
        self.name = name
name → different for each object
species → same for all

🔹 5. Modify & Delete Properties
Modify:
p1.age = 40
Delete:
del p1.age

6. Methods (Functions in Class)
Methods are functions inside a class
They define object behavior
Example:
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello " + self.name)
        
🔹 7. Methods with Parameters
class Calculator:
    def add(self, a, b):
        return a + b
        
🔹 8. Methods Accessing Properties
def get_info(self):
    return f"{self.name} is {self.age} years old"
    
🔹 9. Methods Modifying Properties
def birthday(self):
    self.age += 1
    
Summary
Class → Blueprint
Object → Instance
__init__() → runs when object is created
self → refers to current object
Properties → variables (data)
Methods → functions (behavior)
'''