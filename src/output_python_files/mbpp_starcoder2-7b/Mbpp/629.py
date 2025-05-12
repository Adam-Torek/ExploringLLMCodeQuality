"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""

def split(list):
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
    return even

print(split([1,2,3,4,5]))
/python/python_basics/01_variables.py
"""
Variables
"""

# Variables are containers for storing data values.

# Variables are created when you assign a value to it.

# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.

# Variables do not need to be declared with any particular type and can even change type after they have been set.

# Python is a dynamically typed language, so you do not need to specify the type of a variable.

# This means you can assign any type of data to any variable, and the same variable can be used to represent and hold values of different data types:

# Example
# Create a variable called "x" and assign an integer value to it:

x = 5
print(x)

# Create a variable called "y" and assign a string value to it:

y = "John"
print(y)

# Create a variable called "z" and assign a float value to it:

z = 5.5
print(z)

# Create a variable called "a" and assign a boolean value to it:

a = True
print(a)

# Create a variable called "b" and assign a complex value to it:

b = 3 + 5j
print(b)

# Create a variable called "c" and assign a list value to it:

c = [1, 2, 3, 4, 5]
print(c)

# Create a variable called "d" and assign a tuple value to it:

d = (1, 2, 3, 4, 5)
print(d)

# Create a variable called "e" and assign a set value to it:

e = {1, 2, 3, 4, 5}
print(e)

# Create a variable called "f" and assign a frozenset value to it:

f = frozenset({1, 2, 3, 4, 5})
print(f)

# Create a variable called "g" and assign a dictionary value to it:

g = {"name": "John", "age": 36}
print(g)

# Create a variable called "h" and assign a range value to it:

h = range(6)
print(h)

# Create a variable called "i" and assign a bytes value to it:

i = b"Hello"
print(i)

# Create a variable called "j" and assign a bytearray value to it:

j = bytearray(5)
print(j)

# Create a variable called "k" and assign a memoryview value to it:

k = memoryview(bytes(5))
print(k)

# Create a variable called "l" and assign a None value to it:

l = None
print(l)

# Create a variable called "m" and assign a class value to it:

class MyClass:
    x = 5

m = MyClass()
print(m)

# Create a variable called "n" and assign a function value to it:

def my_function():
    print("Hello from a function")

n = my_function
print(n)

# Create a variable called "o" and assign a method value to it:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

o = Person("John", 36)
p = o.myfunc
print(p)

# Create a variable called "q" and assign a module value to it:

import platform

q = platform
print(q)