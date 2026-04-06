'''
What is Abstraction?
Abstraction means hiding unnecessary details and showing only important features.

Real-life example:
When you use a mobile phone, you don’t know how it works internally.
You just use features like calling, apps, etc.
That’s abstraction.

🔹 Why do we use Abstraction?
Reduces complexity
Improves code readability
Increases security (hides data)
Makes code reusable

🔹 How to Achieve Abstraction in Python?
Python uses:
Abstract Classes
Abstract Methods

Using module  abc (Abstract Base Class)
🔹 Abstract Class
A class that:
Cannot be instantiated (cannot create object)
Contains abstract methods

🔹 Abstract Method
A method:
Declared but not implemented
Must be implemented in child class

🔹 Syntax
from abc import ABC, abstractmetho
class Parent(ABC):   # Abstract class
    @abstractmethod
    def show(self):  # Abstract method
        pass
        
🔹 Key Points
✔ Cannot create object of abstract class
a = Animal() ❌ Error
✔ Child class must implement all abstract methods
✔ Helps in defining rules for subclasses

🔹 Real-Life Analogy
👉 Think of ATM machine
You see options like:
Withdraw
Deposit
But internal banking process is hidden

➡️ That is abstraction

🔹 Short Summary 
Abstraction = Hide details, show essentials
Achieved using ABC module
Uses @abstractmethod
Cannot create object of abstract class
Child class must implement abstract methods
'''
'''
Problem 3: Create an Abstract Class
Create an abstract class Shape with:
* abstract method area()
* abstract method perimeter()
Then create:
* Circle
* Rectangle
'''
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius*self.radius
    def perimeter(self):
        return 2*math.pi*self.radius

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
c = Circle(5)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())
r = Rectangle(4, 6)
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())

'''
Problem 4: Payment System
Design an abstract class Payment:
* method: pay(amount)
Implement:
* CreditCardPayment
* UPIPayment
* NetBankingPayment
'''
from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
class CreditCardPayment(payment):
    def pay(self,amount):
        print(f"Paid {amount} using Credit Card")
class UPIPayment(payment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")
class NetBankingPayment(payment):
    def pay(self,amount):
        print(f"Paid {amount} using Net Banking")
p1=CreditCardPayment()
p1.pay(1000)
p2=UPIPayment()
p2.pay(500)
p3=NetBankingPayment()
p3.pay(100)


# take a class shape as parent class define draw method in it,  child class as circle
#as usual draw method should be in child class also then implement it as method overriding

class Shape:
    def draw(self):
        print("Draw")
class Circle(Shape):
    def draw(self):
        print("Circle")
s=Shape()
c=Circle()
s.draw()
c.draw()
    
    
