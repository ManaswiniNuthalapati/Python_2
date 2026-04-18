'''
Encapsulation (Very Short Notes)
Meaning: Protect data inside a class
Idea: Keep data + methods together
Purpose: Control how data is accessed (avoid mistakes)

Key Points
Hide internal details
Prevent direct access
Use methods to access data
Improves safety & control

Trick: “Hide data + control access = Encapsulation”

Private Variable
Use __ (double underscore)
class A:
    def __init__(self):
        self.__x = 10

Cannot access directly:

obj.__x   ❌

✅ Access using method
class A:
    def __init__(self):
        self.__x = 10
    
    def get_x(self):
        return self.__x
'''