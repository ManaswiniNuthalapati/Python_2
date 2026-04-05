'''
Python Inheritance
🔹 What is Inheritance?
Inheritance means one class can use properties and methods of another class.
It helps in code reuse (no need to rewrite code).

Terms:
Parent Class (Base Class) → Original class
Child Class (Derived Class) → Class that inherits

🔹 Creating a Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()

 Output:
John Doe

🔹 Creating a Child Class
 Syntax:
class ChildClass(ParentClass):
    pass
Example:
class Student(Person):
    pass
x = Student("Mike", "Olsen")
x.printname()
 Child class automatically gets all methods & properties of parent

🔹 Adding __init__() in Child Class
If you add __init__() in child:
 It overrides parent’s constructor

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
🔹 Using super() (Important ⭐)
Better way instead of calling parent manually:
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

 super() automatically calls parent class
 Cleaner and recommended way

🔹 Adding New Properties
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year
        
🔹 Adding New Methods
class Student(Person):
    def welcome(self):
        print("Welcome", self.firstname, self.lastname)
        
🔹 Method Overriding (Very Important ⭐)
Child can change parent method behavior
class Student(Person):
    def printname(self):
        print("Student:", self.firstname, self.lastname)
👉 Child method will run instead of parent

🔹 Key Points to Remember

✔ Inheritance = reuse code
✔ Child class gets all parent features
✔ pass → used when no extra code
✔ super() → best way to call parent
✔ You can:
add new methods
add new variables
override existing methods

Real-Life Example
Parent: Vehicle
Child: Car, Bike
All vehicles have speed, engine
Car adds doors, Bike adds helmet rule
'''