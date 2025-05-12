"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""

def index_multiplication(tuple1, tuple2):
    return tuple(map(lambda x, y: (x[0] * y[0], x[1] * y[1]), tuple1, tuple2))

assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))
/python/python_basics/02_variables/01_variables.py
"""
Write a program to print the sum of two numbers.
"""

a = 10
b = 20

print(a + b)
/python/python_basics/03_operators/01_operators.py
"""
Write a program to print the sum of two numbers.
"""

a = 10
b = 20

print(a + b)
/python/python_basics/04_conditionals/01_conditionals.py
"""
Write a program to print the sum of two numbers.
"""

a = 10
b = 20

if a > b:
    print(a)
else:
    print(b)
/python/python_basics/05_loops/01_loops.py
"""
Write a program to print the sum of two numbers.
"""

a = 10
b = 20

for i in range(10):
    print(i)
/python/python_basics/06_functions/01_functions.py
"""
Write a program to print the sum of two numbers.
"""

def add(a, b):
    return a + b

print(add(10, 20))
/python/python_basics/07_classes/01_classes.py
"""
Write a program to print the sum of two numbers.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(self.name, self.age)

person = Person("John", 30)
person.print_details()
/python/python_basics/08_modules/01_modules.py
"""
Write a program to print the sum of two numbers.
"""

import math

print(math.sqrt(25))
/python/python_basics/09_files/01_files.py
"""
Write a program to print the sum of two numbers.
"""

with open("test.txt", "w") as file:
    file.write("Hello World")

with open("test.txt", "r") as file:
    print(file.read())
/python/python_basics/01_hello_world/01_hello_world.py
"""
Write a program to print the sum of two numbers.
"""

print("Hello World")
/python/python_basics/03_operators/02_operators.py
"""
Write a program to print the sum of two numbers.
"""

a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
/python/python_basics/04_conditionals/02_conditionals.py
"""
Write a program to print the sum of two numbers.
"""

a = 10
b = 20

if a > b:
    print(a)
elif a == b:
    print("Equal")
else:
    print(b)
/python/python_basics/