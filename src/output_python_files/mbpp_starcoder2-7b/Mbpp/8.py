"""
Write a function to find squares of individual elements in a list.
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def square_nums(nums):
    return [num**2 for num in nums]

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
<file_sep>/python/0001_python_basics/0002_variables_and_types/0001_variables.py
"""
Variables
"""

# Variables are used to store information to be referenced and manipulated in a computer program.

# Variables are created when you assign a value to it.

# Python variables do not need explicit declaration to reserve memory space.
# The declaration happens automatically when you assign a value to a variable.

# The equal sign (=) is used to assign values to variables.

# Example

# Create a variable called "x" and assign the value 5 to it.
x = 5

# Create a variable called "y" and assign the value 10 to it.
y = 10

# Create a variable called "z" and assign the value 15 to it.
z = 15

# Print the value of x, y and z
print(x)
print(y)
print(z)

# Output:
# 5
# 10
# 15

# Multiple Assignment

# Python allows you to assign a single value to several variables simultaneously.

# Example

# Create three variables and assign the same value to all of them.
x = y = z = 10

# Print the value of x, y and z
print(x)
print(y)
print(z)

# Output:
# 10
# 10
# 10

# Assigning Multiple Values to Multiple Variables

# Python allows you to assign a single value to several variables simultaneously.

# Example

# Create three variables and assign different values to each one.
x, y, z = 10, 20, 30

# Print the value of x, y and z
print(x)
print(y)
print(z)

# Output:
# 10
# 20
# 30

# Unpacking a Collection

# If you have an iterable object (list, tuple, dictionary, etc.), you can unpack it into different variables.

# Example

# Create a list of three variables.
list = [10, 20, 30]

# Unpack the list and use the variables x, y and z for the list values.
x, y, z = list

# Print the values of x, y and z
print(x)
print(y)
print(z)

# Output:
# 10
# 20
# 30

# Unpacking a Dictionary

# If you have a dictionary object, you can unpack it into different variables.

# Example

# Create a dictionary of three variables.
dict = {'x': 10, 'y': 20, 'z': 30}

# Unpack the dictionary and use the variables x, y and z for the dictionary values.
x, y, z = dict

# Print the values of x, y and z
print(x)
print(y)
print(z)

# Output:
# 10
# 20
# 30

# Unpacking a String

# If you have a string object, you can unpack it into different variables.

# Example

# Create a string of three variables.
string = 'abc'

# Unpack the string and use the variables x, y and z for the string values.
x, y, z = string

# Print the values of x, y and z
print(x)
print(y)
print(z)

# Output:
# a
# b
# c

# Unpacking a Tuple

# If you have a tuple object, you can unpack it into different variables.

# Example