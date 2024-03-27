"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""

def count(lst):
    count = 0
    for i in lst:
        if i == True:
            count += 1
    return count

print(count([True,False,True]))
<file_sep>/python/python_basics/01_variables.py
"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a + b)
<file_sep>/python/python_basics/05_if_else.py
"""
Write a python program to check whether a number is even or odd.
"""

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
<file_sep>/python/python_basics/03_operators.py
"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a + b)

"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a - b)

"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a * b)

"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a / b)

"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a // b)

"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a % b)

"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a ** b)
<file_sep>/python/python_basics/02_input.py
"""
Write a python program to print the sum of two numbers.
"""

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(a + b)
<file_sep>/python/python_basics/04_while_loop.py
"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

while a < b:
    print(a)
    a += 1
<file_sep>/python/python_basics/06_for_loop.py
"""
Write a python program to print the sum of two numbers.
"""

for i in range(10):
    print(i)
<file_sep>/python/python_basics/07_functions.py
"""
Write a python function to print the sum of two numbers.
"""

def sum(a, b):
    return a + b

print(sum(10, 20))
<|endoftext|>