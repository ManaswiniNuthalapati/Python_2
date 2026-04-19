'''
What is OOPS?
OOPS = Object-Oriented Programming System
 It is a way of writing code using objects and classes instead of only functions.

Real-life example:
Car  → object
Person  → object

Each object has:
Properties (data) → name, age
Methods (actions) → walk(), speak()

🔹 1. Class & Object
Class
A class is a blueprint/template.
class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age
Here:
Car = class
__init__ = constructor (runs automatically)
self = refers to current object

Object
Object = instance of class
c2 = Car("Ram", 18)
c3 = Car("Sai", 20)
print(c2.name, c2.age)
print(c3.name, c3.age)

Output:
Ram 18
Sai 20

🔹 4 Pillars of OOPS
 1. Inheritance
👉 One class gets properties/methods of another class
class Animal:
    def speak(self):
        print("Animal speaking")
class Dog(Animal):
    pass
d = Dog()
d.speak()

👉 Output:
Animal speaking
Dog is child class
Animal is parent class

Example 
class Employee:
    def work(self):
        print("Employee working")

class Developer(Employee):
    def code(self):
        print("Developer coding")

d = Developer()
d.work()   # parent method
d.code()   # child method


🔹 Types of Inheritance

1. Single Inheritance
👉 One parent → One child
class A:
    def show(self):
        print("A class")
class B(A):
    pass
    
2. Multiple Inheritance
👉 Multiple parents → One child
class A:
    def aa(self):
        print("class A")
class B:
    def bb(self):
        print("class B")
class C(A, B):
    pass
c = C()
c.aa()
c.bb()

3. Multilevel Inheritance
👉 A → B → C (chain)
class A:
    def aa(self):
        print("A")
class B(A):
    def bb(self):
        print("B")
class C(B):
    def cc(self):
        print("C")
        
4. Hierarchical Inheritance
👉 One parent → multiple children
class A:
    def aa(self):
        print("A")
class B(A):
    pass
class C(A):
    pass
    
    
2. Encapsulation
Wrapping data + methods together
 Example:
class Student:
    def __init__(self, name):
        self.name = name  # public variable

Private variable:
class Student:
    def __init__(self):
        self.__marks = 90   # private

Access using method:
def get_marks(self):
    return self.__marks
 
    
3. Polymorphism
Same method name → different behavior

class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
d = Dog()
c = Cat()
d.sound()
c.sound()
Same method sound() but different outputs


4. Abstraction
Hide unnecessary details, show only important parts
Example:

class Car:
    def start(self):
        print("Car started")

 User only uses:
c = Car()
c.start()
 Internal engine logic is hidden → abstraction



 Final Summary 
Concept	            Meaning
Class	            Blueprint
Object	            Instance of class
Inheritance	        Reuse code
Encapsulation	    Hide data
Polymorphism	    Same function, different behavior
Abstraction	        Hide complexity
'''
