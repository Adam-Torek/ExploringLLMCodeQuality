"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""

def sum_div(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return sum

print(sum_div(8))
<file_sep>/python/python_basics/02_variables.py
"""
Variables
"""

# Variables are containers for storing data values.

# Variables do not need to be declared with any particular type and can even change type after they have been set.

# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.

# Variables are case sensitive (age, Age and AGE are three different variables)

# Variables must be assigned before they can be used, otherwise you will get an error.

# The equal sign (=) is used to assign values to variables.

# Example

# Create a variable called "x" and assign an integer value to it:

x = 5

# Create a variable called "y" and assign a string value to it:

y = "John"

# Create a variable called "z" and assign a float value to it:

z = 5.5

# Create a variable called "a" and assign a boolean value to it:

a = True

# Create a variable called "b" and assign a complex value to it:

b = 3+5j

# Create a variable called "c" and assign a list value to it:

c = ["apple", "banana", "cherry"]

# Create a variable called "d" and assign a tuple value to it:

d = ("apple", "banana", "cherry")

# Create a variable called "e" and assign a range value to it:

e = range(6)

# Create a variable called "f" and assign a set value to it:

f = {"apple", "banana", "cherry"}

# Create a variable called "g" and assign a frozenset value to it:

g = frozenset({"apple", "banana", "cherry"})

# Create a variable called "h" and assign a dictionary value to it:

h = {"name" : "John", "age" : 36}

# Create a variable called "i" and assign a bytearray value to it:

i = bytearray(5)

# Create a variable called "j" and assign a memoryview value to it:

j = memoryview(bytes(5))

# Python Variables are Case-Sensitive

# Variable names are case-sensitive.

# Example

# x is different from X:

x = 4 # x is a variable
X = "John" # X is a variable

# Python Variables do not need to be declared with any particular type, and can even change type after they have been set.

# Example

# If you create a variable without a value, Python will assign the None value to it.

# Example

# Create an integer variable:

x = 5

# Create a string variable:

y = "John"

# Create a float variable:

z = 20.5

# Create a boolean variable:

a = True

# Create a complex variable:

b = 3+5j

# Create a list variable:

c = ["apple", "banana", "cherry"]

# Create a tuple variable:

d = ("apple", "banana", "cherry")

# Create a range variable:

e = range(6)

# Create a set variable:

f = {"apple", "banana", "cherry"}

# Create a frozenset variable:

g = frozenset({"apple", "banana", "cherry"})

# Create a dictionary variable:

h = {"name" : "John", "age" : 36}

# Create a bytearray variable:

i = bytearray(5)

# Create a memoryview variable:

j = memoryview(bytes(5))

# Python Variables are Dynamic

# Variables do not need to be declared with any particular type and can even change type after they have been set.

# Example

# Create an integer variable:

x = 5

# Create a string variable