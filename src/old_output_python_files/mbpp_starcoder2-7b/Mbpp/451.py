"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""

def remove_whitespaces(string):
    return string.replace(' ', '')

print(remove_whitespaces(' Google    Flutter '))
<file_sep>/python/001-basics/001-variables.py
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

# Output
# 5
# John

# Multiple Assignment

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Output
# Orange
# Banana
# Cherry

# Output Variables

x = "awesome"
print("Python is " + x)

# Output
# Python is awesome

# Global Variables

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# Output
# Python is awesome

# The global Keyword

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

# Output
# Python is fantastic

# Python is a Dynamically Typed Language

# In dynamically typed languages, variables do not need to be declared with any particular type and can even change type after they have been set.

# Example

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

# Output
# Sally

# Python is a strongly typed language

# In strongly typed languages, variables have a declared type, and the type is checked at compile time, so violating type often raises a compiler error.

# Example

x = 4 # x is of type int
x = "Sally" # This will cause an error
print(x)

# Output
# TypeError: can only concatenate str (not "int") to str

# Python Numbers

# Integers

x = 1 # int
y = 35656222554887711 # int
z = -3255522 # int

print(type(x))
print(type(y))
print(type(z))

# Output
# <class 'int'>
# <class 'int'>
# <class 'int'>

# Floats

x = 1.10 # float
y = 1.0 # float
z = -35.59 # float

print(type(x))
print(type(y))
print(type(z))

# Output
# <class 'float'>
# <class 'float'>
# <class 'float'>

# Complex Numbers

x = 3+5j # complex
y = 5j # complex
z = -5j # complex

print(type(x))
print(type(y))
print(type(z))

# Output
# <class 'complex'>
# <class 'complex'>
# <class 'complex'>

# Python Strings

# Strings in Python are identified as a contiguous set of characters represented in the quotation marks.

# Python allows for either pairs of single or double quotes.

# Strings are arrays of bytes representing Unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

# Example

a = "Hello, World!"
print(a[1])

# Output
# e

# Negative Indexing

# Use negative indexes to start the slice from the end of the string:

# Example

b = "Hello, World!"
print(b[-5])

# Output
# W