"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""

def power(a,b):
    return a**b

print(power(3,4))
<file_sep>/python/01_python_basics/02_variables_and_types/01_variables.py
"""
Variables are used to store information to be referenced and manipulated in a
computer program.

Variables are created when you assign a value to it.

Variables do not need to be declared with any particular type and can even change
type after they have been set.
"""

# Assigning a value to a variable
x = 5
y = "John"
print(x)
print(y)

# Overwriting a variable
x = 4
print(x)

# Multiple Assignments
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Output Variables
x = "awesome"
print("Python is " + x)

# Global Variables
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# The global Keyword
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
<file_sep>/python/01_python_basics/03_operators/02_arithmetic_operators.py
"""
Arithmetic operators are used to perform mathematical operations like addition,
subtraction, multiplication etc.
"""

# Addition
x = 15
y = 4
print(x + y)

# Subtraction
x = 15
y = 4
print(x - y)

# Multiplication
x = 15
y = 4
print(x * y)

# Division
x = 15
y = 4
print(x / y)

# Modulus
x = 15
y = 4
print(x % y)

# Exponentiation
x = 15
y = 4
print(x ** y)

# Floor Division
x = 15
y = 4
print(x // y)
<file_sep>/python/01_python_basics/03_operators/01_assignment_operators.py
"""
Assignment operators are used to assign values to variables.
"""

# Simple Assignment
x = 5
print(x)

# Assignment by adding
x += 3
print(x)

# Assignment by subtracting
x -= 3
print(x)

# Assignment by multiplying
x *= 3
print(x)

# Assignment by dividing
x /= 3
print(x)

# Assignment by modulus
x %= 3
print(x)

# Assignment by exponentiation
x **= 3
print(x)

# Assignment by floor division
x //= 3
print(x)
<file_sep>/python/01_python_basics/02_variables_and_types/03_strings.py
"""
Strings are used in Python to record text information, such as names.
Strings in Python are actually a sequence, which basically means Python
keeps track of every element in the string as a sequence.

For example, Python understands the string "hello' to be a sequence of letters
in a specific order. This means we will be able to use indexing to grab
parts of the string.
"""

# Creating a String
a = "Hello, World!"
print(a)

# String Length
print(len(a))

# String Indexing
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])
print(a[9])
print(a[10])
print(a[11])
print(a[12])
print(a[13])

# Negative Indexing
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
print(a[-6])
print(a[-7])
print(a[-8])
print