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
        

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog bark")
d = Dog()
d.sound()
    
'''
Create class:
Student
Attributes:
name
marks
Method:
grade()
If marks > 50 → Pass
Else → Fail
'''
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        if self.marks>50:
            print("Pass")
        else:
            print("Fail")
s1=Student("Manu",79)
s1.grade()

'''
Question 2 — ATM Machine
Create class:
ATM
Methods:
deposit()
withdraw()
check_balance()
Use encapsulation.
'''
class ATM:
        def __init__(self, balance):
            self.__balance = balance

        def deposit(self, amount):
            self.__balance += amount
            print("Deposited:", amount)
            
        def withdraw(self, amount):
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawn:", amount)
            else:
                print("Insufficient Balance")

        def check_balance(self):
            print("Current Balance:", self.__balance)
atm = ATM(1000)
atm.deposit(500)
atm.withdraw(300)
atm.check_balance()

'''
Question 3 — Employee System
Parent Class:
Employee
Method:
work()
Child Class:
Developer
Manager
Override method.
'''
class Employee:
    def work(self):
        print("Employee works")
class Developer(Employee):
    def work(self):
        print("Developer works")
class Manager(Employee):
    def work(self):
        print("Manager works")
d1=Developer()
d1.work()
m1=Manager()
m1.work()

'''
Question 4 — Shape Example (Abstraction)
Create Abstract Class:
Shape
Method:
area()
Create child classes:
Circle
Rectangle
'''
from abc import ABC, abstractmethod
import math
class Shape:
    @abstractmethod
    def area(self):
        pass
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius*self.radius
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
c=Circle(5)
print(c.area())
r=Rectangle(2,3)
print(r.area())
    
'''
Question 5 — Shopping Cart
Create class:
Product
Attributes:
name
price
Method:
display()
Create 3 objects.
'''
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print("Name",self.name)
        print("Price",self.price)
p1=Product("Laptop",70000)
p2=Product("Mobile",50000)
p3=Product("Airpods",15000)
p1.display()
p2.display()
p3.display()

'''
1. Class & Object
Create a class Student
Attributes:
name
age
marks
Method:
display()
Create 3 objects and print details.
'''
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
s=Student("Manu",19,90)
s1=Student("John",20,83)
s2=Student("Joe",20,99)
s.display()
s1.display()
s2.display()
                #OR
class Student:
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
s=Student()
s.name="Manu"
s.age=19
s.marks=90
s1=Student()
s1.name="John"
s1.age=20
s1.marks=83
s2=Student()
s2.name="Joe"
s2.age=20
s2.marks=99
s.display()
s1.display()
s2.display()

'''
2. Constructor
Create class Employee
Constructor should accept:
name
department
salary
Create method:
show_details()
Create 2 objects.
'''
class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
    def show_details(self):
        print("Name:",self.name)
        print("Department:",self.department)
        print("Salary:",self.salary)
e=Employee("MN","HR",100000)
e1=Employee("M","Manager",70000)
e.show_details()
e1.show_details()
        
'''
5. Inheritance (Single Inheritance)
Create Parent class:
Person
Attributes:
name
age
Method:
display()
Create Child class:
Student
Add:
marks
Create object and display details.
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name",self.name)
        print("Age",self.age)
class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks
    def display(self):
        super().display()
        print("Marks",self.marks)
s=Student("Manu",20,99)
s.display()

'''
Multi-Level Inheritance
Create:
Grandparent → Animal
Parent → Dog
Child → Puppy
Methods:
Animal → eat()
Dog → bark()
Puppy → weep()
Create object and call all methods.
'''
class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")
a=Animal()
a.eat()
d=Dog()
d.bark()
p=Puppy()
p.weep()

'''
7. Polymorphism (Method Overriding)
Create Parent class:
Shape
Method:
draw()
Create Child classes:
Circle
Rectangle
Override draw() method.
'''
class Shape:
    def draw(self):
        print("Drawing a shape")
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")
class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")
c=Circle()
c.draw()
r=Rectangle()
r.draw()

'''
8. Polymorphism (Operator Polymorphism)
Create class Calculator
Create method:
add()
It should:
Add 2 numbers
Add 3 numbers
(Hint: Use default arguments)
class Calculator:
    def __init__(self,a,b,c=0):
        self.a=a
        self.b=b
        self.c=c
    def add(self):
        sum=a+b+c
c=Calculator(10,20,30)
c.add()
c1=Calculator(10,20)
c1.add()
        '''

# Create a class Car with attributes brand and price. Print details.
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def display(self):
        print(self.brand, self.price)
c1 = Car("Toyota", 1000000)
c1.display()
        
        
