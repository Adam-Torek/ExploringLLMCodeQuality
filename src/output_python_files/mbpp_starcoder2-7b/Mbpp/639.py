"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan','rebecca', 'Diana', 'Joanne', 'keith'])==16
"""

def sample_nam(names):
    sum = 0
    for name in names:
        if name[0].isupper():
            sum += len(name)
    return sum

print(sample_nam(['sally', 'Dylan','rebecca', 'Diana', 'Joanne', 'keith']))
/python_basics/02_variables_and_data_types/02_02_variables.py
"""
Variables
"""

# Variables are used to store information to be referenced and manipulated in a computer program.

# Rules for Python variables
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Assigning values to variables
# Python variables do not need explicit declaration to reserve memory space.
# The declaration happens automatically when you assign a value to a variable.

# The equal sign (=) is used to assign values to variables.

# Example
# Create a variable called "x" and assign an integer value to it.
x = 5

# Create a variable called "y" and assign a string value to it.
y = "John"

# Create a variable called "z" and assign a float value to it.
z = 3.2

# Create a variable called "a" and assign a boolean value to it.
a = True

# Create a variable called "b" and assign a complex value to it.
b = 3+5j

# Create a variable called "c" and assign a list value to it.
c = ["apple", "banana", "cherry"]

# Create a variable called "d" and assign a tuple value to it.
d = ("apple", "banana", "cherry")

# Create a variable called "e" and assign a range value to it.
e = range(6)

# Create a variable called "f" and assign a set value to it.
f = {"apple", "banana", "cherry"}

# Create a variable called "g" and assign a frozenset value to it.
g = frozenset({"apple", "banana", "cherry"})

# Create a variable called "h" and assign a dictionary value to it.
h = {"name" : "John", "age" : 36}

# Create a variable called "i" and assign a bytearray value to it.
i = bytearray(5)

# Create a variable called "j" and assign a memoryview value to it.
j = memoryview(bytes(5))

# Print the variable values
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)

# The type() function can be used to get the type of a variable.
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))

# The id() function can be used to get the unique id of a variable.
print(id(x))
print(id(y))
print(id(z))
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))
print(id(g))
print(id(h))
print(id(i))
print(id(j))

# The isinstance() function can be used to check if a variable is an instance of a given class.
print(isinstance(x, int))
print(isinstance(y, str