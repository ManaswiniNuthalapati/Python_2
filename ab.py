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
    
