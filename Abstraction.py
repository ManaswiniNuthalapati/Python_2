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
