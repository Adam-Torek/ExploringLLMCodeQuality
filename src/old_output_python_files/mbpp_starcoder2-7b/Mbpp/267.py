"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""

def square_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

print(square_Sum(2))
<file_sep>/Python/Python_Basics/02_Variables/01_Variables.py
"""
Variables are used to store information to be referenced and manipulated in a computer program.
"""

# Variables are declared by using the assignment operator (=)

# Example

# Declare a variable and initialize it
f = 0
print(f)

# Re-declaring the variable works
f = "abc"
print(f)

# Error: variables of different types cannot be combined
# print("This is a string" + 123)

# Global vs. local variables

# Global variables are declared and defined outside a function.
# Local variables are declared and defined inside a function.
# Global variables can be accessed inside or outside of a function.
# Local variables can be accessed only inside the function.

# Example: Global vs. local variables

# Global variable

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Local variable

# Local variable
def foo():
    # local variable
    y = "local"
    print(y)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable
    print(x)

foo()

# Global variable
x = "global"

def foo():
    # using a global variable