"""
Write a python function to convert the given string to lower case.
assert is_lower("InValid") == "invalid"
"""

def is_lower(string):
    return string.lower()

print(is_lower("InValid"))
<file_sep>/python/python_basics/02_variables/02_variables.py
"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a + b)
<file_sep>/python/python_basics/03_operators/03_operators.py
"""
Write a python program to print the result of the following operations.
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
<file_sep>/python/python_basics/04_conditional_statements/04_conditional_statements.py
"""
Write a python program to print the result of the following operations.
"""

a = 10
b = 20

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
<file_sep>/python/python_basics/01_hello_world/01_hello_world.py
"""
Write a python program to print "Hello World"
"""

print("Hello World")
<file_sep>/python/python_basics/05_loops/05_loops.py
"""
Write a python program to print the result of the following operations.
"""

a = 10
b = 20

while a < b:
    print(a)
    a += 1

for i in range(a, b):
    print(i)
<file_sep>/python/python_basics/06_functions/06_functions.py
"""
Write a python function to print the result of the following operations.
"""

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print(add(10, 20))
print(sub(10, 20))
print(mul(10, 20))
print(div(10, 20))
<file_sep>/python/python_basics/07_classes/07_classes.py
"""
Write a python class to represent a student.
"""

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

student = Student("John", 20, 90)
student.print_details()
<file_sep>/python/python_basics/08_modules/08_modules.py
"""
Write a python program to import the math module and print the value of pi.
"""

import math

print(math.pi)
<file_sep>/python/python_basics/09_files/09_files.py
"""
Write a python program to read the contents of a file.
"""

with open("test.txt", "r") as file:
    print(file.read())
<file_sep>/python/python_basics/09_files/09_files_write.py
"""
Write a python program to write the contents of a file.
"""

with open("test.txt", "w") as file:
    file.write("Hello World")
<file_sep>/python/python_basics/08_modules/08_modules_import.py
"""
Write a python program to import the math module and print the value of pi.
"""

from math import pi

print(pi)
<file_sep>/python/python_basics/09_files/09_files_append.py
"""
Write a python program to append the contents of a file.
"""

with open("test.txt", "a") as file:
    file.write("Hello World")
<|endoftext|>