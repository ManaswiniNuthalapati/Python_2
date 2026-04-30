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