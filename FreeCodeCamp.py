'''
Write a Python program to create a class named MusicalInstrument.

Requirements:

1. Create an __init__ method that initializes:
    name → name of the instrument
    instrument_type → family/type of the instrument
2. Create a method named play() that prints:
    "The [instrument name] is fun to play!"
3. Create another method named get_fact() that returns:
    "The [instrument name] is part of the [instrument type] family of instruments."
4. Create two objects:
    instrument_1 with values "Oboe" and "woodwind"
    instrument_2 with values "Trumpet" and "brass"
5. Call the play() method using instrument_1.
6. Print the result of the get_fact() method using instrument_1.
'''
class MusicalInstrument:
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    def play(self):
        print(f'The {self.name} is fun to play!')

    def get_fact(self):
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'

instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

instrument_1.play()
print(instrument_1.get_fact())

