'''
Python Polymorphism

🔹 Definition
Polymorphism means “many forms”.
In programming, it refers to:
👉 Same method / function / operator behaving differently for different objects.

🔹 Key Idea
One interface → Multiple implementations
Same method name → Different behavior depending on object


🔹 1. Function Polymorphism
Example: len() function
x = "Hello"
print(len(x))   # String → characters count

mytuple = ("a", "b", "c")
print(len(mytuple))   # Tuple → number of items

mydict = {"a":1, "b":2}
print(len(mydict))   # Dictionary → key-value pairs

✅ Same function → works for different data types


🔹 2. Class Polymorphism
👉 Different classes can have same method name

Example:
class Car:
    def move(self):
        print("Drive!")

class Boat:
    def move(self):
        print("Sail!")

class Plane:
    def move(self):
        print("Fly!")

for x in (Car(), Boat(), Plane()):
    x.move()

✅ Same method move() → different outputs


🔹 3. Polymorphism with Inheritance
👉 Child classes override parent method

Example:
class Vehicle:
    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

✅ Child classes can modify behavior of parent method


🔹 4. Method Overriding (Runtime Polymorphism)
Same method in parent & child class
Child class provides new implementation

👉 Happens at runtime


🔹 5. Operator Polymorphism
Example:
print(2 + 3)        # Addition
print("Hi" + "All") # String concatenation

✅ Same operator + → different behavior

🔹 Advantages
Code reusability
Flexibility
Cleaner & scalable code
Reduces complexity

🔹 Real-Life Example
👉 Payment system:

processPayment() method
Credit Card → bank validation
UPI → gateway
Wallet → balance check

Same method → different behavior

🔹 Important Points to Remember
Python supports runtime polymorphism
Method overloading is not direct (use default arguments)
Mostly used with:
Classes
Inheritance
Functions
'''
'''
Create a base class Animal with method sound().
Override it in Dog and Cat.
'''
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
a = Animal()
d = Dog()
c = Cat()
a.sound()
d.sound()
c.sound()

# Create different classes (Car, Bike) with same method move().
class Car:
    def move(self):
        print("Car is moving")
class Bike:
    def move(self):
        print("Bike is moving")
for vehicle in (Car(), Bike()):
    vehicle.move()