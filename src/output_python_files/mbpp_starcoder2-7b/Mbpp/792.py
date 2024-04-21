"""
Write a python function to count the number of lists in a given number of lists.
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
"""

def count_list(lists):
    count = 0
    for i in lists:
        if type(i) == list:
            count += 1
    return count

print(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]))
<file_sep>/python/python_basics/03_variables/02_variables.py
"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a + b)
<file_sep>/python/python_basics/06_loops/02_for_loop.py
"""
Write a python program to print the numbers from 1 to 10.
"""

for i in range(1, 11):
    print(i)
<file_sep>/python/python_basics/05_conditionals/02_if_else.py
"""
Write a python program to check if a number is positive, negative or zero.
"""

number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
<file_sep>/python/python_basics/06_loops/01_while_loop.py
"""
Write a python program to print the numbers from 1 to 10.
"""

i = 1
while i <= 10:
    print(i)
    i += 1
<file_sep>/python/python_basics/04_functions/01_functions.py
"""
Write a python function to print the sum of two numbers.
"""

def sum(a, b):
    return a + b

print(sum(10, 20))
<file_sep>/python/python_basics/03_variables/03_variables.py
"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a + b)

a = 10
b = 20

print(a + b)
<file_sep>/python/python_basics/05_conditionals/01_if.py
"""
Write a python program to check if a number is positive, negative or zero.
"""

number = 0

if number > 0:
    print("Positive")
<file_sep>/python/python_basics/04_functions/02_functions.py
"""
Write a python function to print the sum of two numbers.
"""

def sum(a, b):
    print(a + b)

sum(10, 20)
<file_sep>/python/python_basics/03_variables/01_variables.py
"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a + b)
<file_sep>/python/python_basics/06_loops/03_for_loop.py
"""
Write a python program to print the numbers from 1 to 10.
"""

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i