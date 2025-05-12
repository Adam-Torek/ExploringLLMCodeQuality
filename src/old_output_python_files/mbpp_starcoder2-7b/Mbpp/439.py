"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""

def multiple_to_single(list):
    return int(''.join(map(str, list)))

print(multiple_to_single([11, 33, 50]))
<file_sep>/python/python_basics/002_variables.py
"""
Variables
"""

# Variables are containers for storing data values.

# Variables do not need to be declared with any particular type and can even change type after they have been set.

# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.

# Variables must be assigned before they can be used, otherwise you will get an error.

# The equal sign (=) is used to assign values to variables.

# Example

x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type and can even change type after they have been set.

# Example

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

# Output: Sally

# Python is a dynamically typed language, so you do not need to specify the type of a variable.

# This means you can assign any type of data to any variable.

# Example

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

# Output: Sally

# Python has a number of type built-in methods to calculate different values.

# Example

x = 1 # x is of type int
x = float(x) # x is now of type float
y = 2.8 # y is of type float
y = int(y) # y is now of type int
z = 3 # z is of type int
z = float(z) # z is now of type float
print(x)
print(y)
print(z)

# Output: 1 2 3.0

# Python has many built-in modules and functions.

# To use a function you must import the module.

# Example

import math
print(math.sqrt(64))

# Output: 8.0

# Python has a set of built-in functions you can also use.

# Example

print(min(5, 10, 25))

# Output: 5

# Python has a set of built-in methods you can use on dictionaries.

# Example

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)

# Output: dict_keys(['brand','model', 'year'])

# Python has a set of built-in methods you can use on lists.

# Example

cars = ["Ford", "Volvo", "BMW"]

x = cars.index("Volvo")

print(x)

# Output: 1

# Python has a set of built-in methods you can use on tuples.

# Example

thistuple = ("apple", "banana", "cherry")

x = thistuple.count("apple")

print(x)

# Output: 1

# Python has a set of built-in methods you can use on sets.

# Example

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Output: {'apple', 'cherry', 'banana', 'orange'}

# Python has a set of built-in methods you can use on strings.

# Example

a = "Hello, World!"
print(a.upper())

# Output: HELLO, WORLD!

# Python has a set of built-in methods you can use on numbers.

# Example

x = 20

x = x.bit_length()

print(x)

# Output: 5

# Python has a set of built-in methods you can use on bytes and bytearray.

# Example

x =