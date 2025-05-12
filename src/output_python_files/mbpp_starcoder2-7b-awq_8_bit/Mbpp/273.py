"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""

def substract_elements(tuple1, tuple2):
    return tuple(tuple1[i] - tuple2[i] for i in range(len(tuple1)))

print(substract_elements((10, 4, 5), (2, 5, 18)))
/python/python_basics/02_variables/02_variables.py
"""
Write a program that asks the user for their name and age.
Print out a message that says "Hello, my name is [name] and I am [age] years old."
"""

name = input("What is your name? ")
age = input("How old are you? ")

print("Hello, my name is " + name + " and I am " + age + " years old.")
/python/python_basics/03_conditionals/03_conditionals.py
"""
Write a program that asks the user for their age.
If they are under 18, print out "You are not old enough to vote."
If they are 18 or older, print out "You are old enough to vote."
"""

age = input("How old are you? ")

if int(age) < 18:
    print("You are not old enough to vote.")
else:
    print("You are old enough to vote.")
/python/python_basics/05_lists/05_lists.py
"""
Write a function that takes in a list of numbers and returns the sum of the list.
assert sum_list([1, 2, 3, 4]) == 10
"""

def sum_list(list):
    return sum(list)

print(sum_list([1, 2, 3, 4]))
/python/python_basics/04_loops/04_loops.py
"""
Write a program that asks the user for a number.
Print out all of the numbers from 0 to the number that the user entered.
"""

number = input("Enter a number: ")

for i in range(int(number) + 1):
    print(i)
/python/python_basics/01_hello_world/01_hello_world.py
"""
Write a program that prints out "Hello, world!"
"""

print("Hello, world!")
/python/python_basics/06_dictionaries/06_dictionaries.py
"""
Write a function that takes in a dictionary and returns the sum of all of the values.
assert sum_values({"a": 1, "b": 2, "c": 3}) == 6
"""

def sum_values(dictionary):
    return sum(dictionary.values())

print(sum_values({"a": 1, "b": 2, "c": 3}))
/python/python_basics/07_functions/07_functions.py
"""
Write a function that takes in a list of numbers and returns the sum of the list.
assert sum_list([1, 2, 3, 4]) == 10
"""

def sum_list(list):
    return sum(list)

print(sum_list([1, 2, 3, 4]))
/python/python_basics/08_classes/08_classes.py
"""
Write a class that represents a rectangle.
The class should have two attributes: width and height.
The class should have a method that returns the area of the rectangle.
assert Rectangle(10, 20).area() == 200
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

print(Rectangle(10, 20).area())
/python/python_basics/09_modules/09_modules.py
"""
Write a function that takes in a list of numbers and returns the sum of the list.
assert sum_list([1, 2, 3, 4]) == 10
"""

from sum_list import sum