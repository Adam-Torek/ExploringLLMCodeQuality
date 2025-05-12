"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""

def common_in_nested_lists(nested_list):
    """
    :param nested_list: list of lists
    :return: set of common elements
    """
    return set.intersection(*map(set, nested_list))


if __name__ == '__main__':
    print(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))
/python/python_101/001_basics/001_variables.py
"""
Variables
"""

# Variables are used to store data.
# Variables are created when you assign a value to it.
# Variables do not need to be declared with any particular type and can even change type after they have been set.

# Python is a dynamically typed language.
# This means that you do not need to specify the type of a variable when you create it.
# Python will automatically assign the type.

# Variables can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Assign Value to a Variable
# Python variables do not need explicit declaration to reserve memory space.
# The declaration happens automatically when you assign a value to a variable.

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
c = [1, 2, 3, 4, 5]

# Create a variable called "d" and assign a tuple value to it:
d = (1, 2, 3, 4, 5)

# Create a variable called "e" and assign a set value to it:
e = {1, 2, 3, 4, 5}

# Create a variable called "f" and assign a dictionary value to it:
f = {"name": "John", "age": 36}

# Create a variable called "g" and assign a frozenset value to it:
g = frozenset({"apple", "banana", "cherry"})

# Create a variable called "h" and assign a range value to it:
h = range(6)

# Create a variable called "i" and assign a bytes value to it:
i = bytes(5)

# Create a variable called "j" and assign a bytearray value to it:
j = bytearray(5)

# Create a variable called "k" and assign a memoryview value to it:
k = memoryview(bytes(5))

# Create a variable called "l" and assign a None value to it:
l = None

# Create a variable called "m" and assign a