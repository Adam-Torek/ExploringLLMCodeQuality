"""
Write a function to convert a given string to a tuple of characters.
assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
"""

def string_to_tuple(string):
    return tuple(string)

print(string_to_tuple("python 3.0"))
<file_sep>/python_basics/01_python_basics/02_variables/02_variable_types.py
"""
Write a program to print the type of the following variables:
a = 10
b = 10.5
c = "Hello"
d = True
"""

a = 10
b = 10.5
c = "Hello"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
<file_sep>/python_basics/01_python_basics/03_operators/02_arithmetic_operators.py
"""
Write a program to print the result of the following arithmetic operations:
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
"""

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
<file_sep>/python_basics/01_python_basics/03_operators/03_comparison_operators.py
"""
Write a program to print the result of the following comparison operations:
a = 10
b = 5
print(a == b)
print(a!= b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
"""

a = 10
b = 5

print(a == b)
print(a!= b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
<file_sep>/python_basics/01_python_basics/02_variables/01_variable_declaration.py
"""
Write a program to declare a variable named "name" and assign it a value of "Python".
"""

name = "Python"
<file_sep>/python_basics/01_python_basics/03_operators/01_assignment_operators.py
"""
Write a program to print the result of the following assignment operations:
a = 10
b = 5
a += b
a -= b
a *= b
a /= b
a //= b
a %= b
a **= b
"""

a = 10
b = 5

a += b
a -= b
a *= b
a /= b
a //= b
a %= b
a **= b

print(a)
<file_sep>/python_basics/01_python_basics/03_operators/04_logical_operators.py
"""
Write a program to print the result of the following logical operations:
a = 10
b = 5
print(a and b)
print(a or b)
print(not a)
"""

a = 10
b = 5

print(a and b)
print(a or b)
print(not a)
<file_sep>/python_basics/01_python_basics/02_variables/03_variable_scope.py
"""
Write a program to print the value of the variable "name" after the following code:
name = "Python"
print(name)
"""

name = "Python"
print(name)
<file_sep>/python_basics/01_python_basics/02_variables/04_variable_reassignment.py
"""
Write a program to print the value of the variable "name" after the following code:
name = "Python"
name = "Java"
print(name)
"""

name = "Python"
name = "Java"
print(name)
<file_sep>/python_basics/01_python_basics/03_operators/05_membership_operators.py