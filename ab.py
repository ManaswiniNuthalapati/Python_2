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
