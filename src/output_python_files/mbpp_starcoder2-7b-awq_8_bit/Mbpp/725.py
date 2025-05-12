"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53','multi', 'Processor']
"""

def extract_quotation(string):
    return re.findall(r'"(.*?)"', string)

print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))
/python/python_basics/002_variables.py
"""
Variables
"""

# Variables are used to store values.

# Rules for naming a variable
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Assigning values to variables
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

# Example
# Create an integer:
x = 5
print(x)

# Create a float:
y = 2.8
print(y)

# Create a string:
z = "Hello World"
print(z)

# Multiple Assignment
# Python allows you to assign values to multiple variables in one line

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Output Variables
# The Python print statement is often used to output variables.

x = 5
y = 10

print(x)
print(y)

# Output multiple variables
x = 5
y = 10
z = 50

print(x)
print(y)
print(z)

# Output variables from different data types
x = 5
y = "John"
print(x)
print(y)

# Output multiple variables from different data types
x = 5
y = "John"
print(x)
print(y)

# Output variables from the same line
x = 5
y = 10
print(x)
print(y)

# Output variables from the same line
x = 5
y = 10
print(x, y)

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-')

# Output variables from the same line
x = 5
y = 10
print(x, y, sep='-