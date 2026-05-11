# Create a Student class with name and marks. Print details.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
s1=Student("Manaswini",90)
s2=Student("Sai",85)
s1.display()
s2.display()

# Create a BankAccount with deposit & withdraw.
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient balance")
            
    def show_balance(self):
        print("Balance:",self.balance)
        
acc=BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()

# Create a class Calculator with a method to add two numbers.
class Calculator:
    def add(self,a,b):
        return a+b
c=Calculator()
print(c.add(10,20))

# Create a class Car with brand and model using constructor.
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
c1=Car("Toyota","Innova")
print(c1.brand)
print(c1.model)

# Create a parent class Animal and child class Dog.
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.sound()
d.bark()

# Different classes with same method name.
class Cat:
    def sound(self):
        print("Meow")
class Cow:
    def sound(self):
        print("Moo")
c1 = Cat()
c2 = Cow()
c1.sound()
c2.sound()