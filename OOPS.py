'''
Python OOP Notes
🔹 Python Classes/Objects
Python is an object-oriented programming language.
Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
🔹 Create a Class
To create a class, use the keyword class:
class MyClass:
  x = 5
  
🔹 Create Object
Now we can use the class named MyClass to create objects:
p1 = MyClass()
print(p1.x)

🔹 The init() Function
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use it to assign values to object properties.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

🔹 The str() Function
Controls what should be returned when the class object is represented as a string.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

🔹 Object Methods
Objects can also contain methods.
Methods in objects are functions that belong to the object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

🔹 The self Parameter
self is a reference to the current instance of the class.
It is used to access variables that belong to the class.
It does not have to be named self, but it has to be the first parameter.

🔹 Modify Object Properties
You can modify properties on objects like this:
p1.age = 40

🔹 Delete Object Properties
You can delete properties on objects:
del p1.age

🔹 Delete Objects
You can delete objects:
del p1

🔹 The pass Statement
class definitions cannot be empty.
If you have a class definition with no content, use pass.
class Person:
  pass
  
Final Summary
Class → Blueprint for objects
Object → Instance of class
init() → Constructor
self → Reference to current object
Methods → Functions inside class
Properties → Variables inside class
'''