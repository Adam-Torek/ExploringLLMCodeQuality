"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""

def sum_series(n):
    sum = 0
    for i in range(n//2):
        sum += n - 2*i
    return sum

print(sum_series(6))
<file_sep>/python/python_basics/01_variables_and_types/01_variables.py
"""
Variables are used to store information to be referenced and manipulated in a computer program.

Variables are created when you assign a value to it.

Python variables do not need explicit declaration to reserve memory space.

The assignment operator (=) is used to assign values to variables.

Variables must be declared before they can be used,

The equal sign (=) is used to assign values to variables.

All variables in Python are objects.

Variables are created when you assign a value to it.

Variables do not need to be declared with any particular type and can even change type after they have been set.

"""

# Example

x = 5
y = "John"
print(x)
print(y)

# Output
# 5
# John

# Example

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

# Output
# Sally

# Example

x = "awesome"
print("Python is " + x)

# Output
# Python is awesome

# Example

x = "Python is "
y = "awesome"
z =  x + y
print(z)

# Output
# Python is awesome

# Example

x = 5
y = 10
print(x + y)

# Output
# 15

# Example

x = 5
y = "John"
print(x + y)

# Output
# TypeError: unsupported operand type(s) for +: 'int' and'str'

# Example

x = 5
y = 10
print(str(x) + y)

# Output
# TypeError: can only concatenate str (not "int") to str

# Example

x = 5
y = 10
print(x + int(y))

# Output
# 15

# Example

x = 5
y = 10
print(x + float(y))

# Output
# 15.0

# Example

x = 5
y = 10
print(x + float(y))

# Output
# 15.0

# Example

x = 5
y = 10
print(x + float(y))

# Output
# 15.0

# Example

x = 5
y = 10
print(x + float(y))

# Output
# 15.0

# Example

x = 5
y = 10
print(x + float(y))

# Output
# 15.0

# Example

x = 5
y = 10
print(x + float(y))

# Output
# 15.0

# Example

x = 5
y = 10
print(x + float(y))

# Output
# 15.0

# Example

x = 5
y = 10
print(x + float(y))

# Output
# 15.0

# Example

x = 5
y = 10
print(x + float(y))

# Output
# 15.0

# Example

x = 5
y = 10
print(x + float(y))

# Output
# 15.0

# Example

x = 5
y = 10
print(x + float(y))

# Output
# 15.0

# Example

x = 5
y = 10
print(x + float(y))

# Output
# 15.0

# Example

x = 5
y