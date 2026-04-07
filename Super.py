'''
#initialise a parent class as Employee-constructor with parameter name, 
# child class as Developer - constructor with parameter prog_lang, user super()
'''
class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, prog_lang):
        super().__init__(name)  
        self.prog_lang = prog_lang
dev1 = Developer("Vinaya", "Python")
print("Name:", dev1.name)
print("Programming Language:", dev1.prog_lang)
