'''
Create a class Student
Attributes:
name
marks
Method:
display()
Create 2 objects and print details.
'''
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
s1=Student("Manaswini",19)
s1.display()
    
'''
Question 2 — Constructor
Create class Employee
Constructor should accept:
name
salary
Method:
show_details()
'''
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_details(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
e1=Employee("Manaswini",50000)
e1.show_details()

'''
Question 3 — Encapsulation
Create class Bank
Private variable:
balance
Methods:
deposit()
withdraw()
show_balance()
'''
class Bank:
    def __init__(self,balance):
        self._balance=balance
        
'''
Question 4 — Inheritance
Create Parent Class:
Vehicle
Method:
start()
Create Child Class:
Car
Method:
drive()
Create an object and call both methods.
'''
class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def drive(self):
        print("Vehicle is driving")
c1=Car()
c1.start()
c1.drive()

'''
Question 5 — Polymorphism
Create class:
Animal
Method:
sound()
Create child classes:
Dog
Cat
Override sound() method.
'''
class Animal:
    def sound(self):
        print("Animal sounds")
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cats meows")
d1=Dog()
d1.sound()
c1=Cat()
c1.sound()
        

    
    