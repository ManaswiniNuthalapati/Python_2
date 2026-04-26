# Create a Student class with name and marks. Print details.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
s1 = Student("Manaswini", 90)
s2 = Student("Sai", 85)
s1.display()
s2.display()