"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""

def remove_odd(lst):
    return [x for x in lst if x % 2 == 0]

print(remove_odd([1,2,3]))
<file_sep>/python/0001_python_basics/0002_variables_and_types/0001_variables.py
"""
Variables are used to store information to be referenced and manipulated in a
computer program.

Variables are created when you assign a value to it.

Variables do not need to be declared with any particular type and can even change
type after they have been set.

"""

# Variables are created when you assign a value to it
x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type and can even
# change type after they have been set
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)
<file_sep>/python/0001_python_basics/0002_variables_and_types/0003_strings.py
"""
Strings in python are identified as a contiguous set of characters represented
in the quotation marks.

Python allows for either pairs of single or double quotes.

Strings are immutable.

"""

# Strings in python are identified as a contiguous set of characters represented
# in the quotation marks.
a = "Hello"
print(a)

# Python allows for either pairs of single or double quotes.
a = 'Hello'
print(a)

# Strings are immutable.
a = "Hello"
print(a)
# a[1] = 'x' # TypeError:'str' object does not support item assignment
<file_sep>/python/0001_python_basics/0002_variables_and_types/0004_numbers.py
"""
Numbers in python can be integers (1 and 2), floats (1.1 and 1.2),
fractions (1/2 and 2/3), or even complex numbers (1+2j and 1.1+2.2j).

"""

# Numbers in python can be integers (1 and 2), floats (1.1 and 1.2),
# fractions (1/2 and 2/3), or even complex numbers (1+2j and 1.1+2.2j).
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
<file_sep>/python/0001_python_basics/0002_variables_and_types/0005_booleans.py
"""
Booleans represent one of two values: True or False.

"""

# Booleans represent one of two values: True or False.
x = True
y = False
print(type(x))
print(type(y))
<file_sep>/python/0001_python_basics/0002_variables_and_types/0006_lists.py
"""
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data,
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets.

"""

# Lists are used to store multiple items in a single variable.
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Lists are created using square brackets.
thislist = ["apple", "banana", "cherry"]
print(thislist)
<file_sep>/python/0001_python_basics/0002_variables_and_types/0007_tuples.py
"""
Tuples are used to store multiple items in a single variable.

Tuples are one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

Tuples are created using parentheses.

"""

# Tuples are used to store multiple items in a single variable.
thistuple = ("apple", "ban