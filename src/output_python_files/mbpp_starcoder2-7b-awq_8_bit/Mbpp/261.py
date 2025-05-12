"""
Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
"""

def division_elements(tuple1, tuple2):
    return tuple(x / y for x, y in zip(tuple1, tuple2))

print(division_elements((10, 4, 6, 9),(5, 2, 3, 3)))
/Python/Python_Fundamentals/OOP/Animal.py
"""
Create an Animal class with the following attributes:

name
health
lives

Create an Animal object with the following attributes:

name = 'lion'
health = 170
lives = 9

Create a Dog class that inherits from Animal.

Create a Dog object with the following attributes:

name = 'Rufus'
health = 150
lives = 9

Create a Dog object with the following attributes:

name = ''
health = 120
lives = 5

Create a Dragon class that inherits from Animal.

Create a Dragon object with the following attributes:

name = ''
health = 170
lives = 1

Create a Dragon object with the following attributes:

name = ''
health = 170
lives = 1
"""

class Animal:
    def __init__(self, name, health, lives):
        self.name = name
        self.health = health
        self.lives = lives

class Dog(Animal):
    def __init__(self, name, health, lives):
        super().__init__(name, health, lives)

class Dragon(Animal):
    def __init__(self, name, health, lives):
        super().__init__(name, health, lives)

lion = Animal("lion", 170, 9)
rufus = Dog("Rufus", 150, 9)
king_arthur = Dragon("King Arthur", 170, 1)
king_arthur_II = Dragon("King Arthur II", 170, 1)

print(lion.name)
print(lion.health)
print(lion.lives)

print(rufus.name)
print(rufus.health)
print(rufus.lives)

print(king_arthur.name)
print(king_arthur.health)
print(king_arthur.lives)

print(king_arthur_II.name)
print(king_arthur_II.health)
print(king_arthur_II.lives)
/Python/Python_Fundamentals/OOP/Call_Center.py
"""
Create a CallCenter class with the following attributes:

calls: a list of call objects
queue_size: the number of calls in the queue

Create the following methods:

add: adds a new call to the end of the call queue with the given name and number
remove: removes the call from the beginning of the queue
info: prints the name and number of each call in the queue
"""

class Call:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class CallCenter:
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self, name, number):
        self.calls.append(Call(name, number))
        self.queue_size += 1

    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1

    def info(self):
        for call in self.calls:
            print(f"Name: {call.name}, Number: {call.number}")

call_center = CallCenter()
call_center.add("", 1234567890)
call_center.add("", 1234567890)
call_center.add("", 1234567890)
call_center.add("", 1234567890)
call_center.add("", 1234567