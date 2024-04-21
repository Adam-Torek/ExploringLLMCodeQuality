"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""

def unique_product(lst):
    unique_lst = []
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
    product = 1
    for i in unique_lst:
        product *= i
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))
<file_sep>/python_basics/01_python_basics/01_python_basics.py
"""
Write a python function to calculate the sum of the digits of a given number.
assert sum_digits(123) == 6
"""

def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

print(sum_digits(123))
<file_sep>/python_basics/02_python_basics/02_python_basics.py
"""
Write a python function to calculate the sum of the digits of a given number.
assert sum_digits(123) == 6
"""

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))
<file_sep>/python_basics/03_python_basics/03_python_basics.py
"""
Write a python function to calculate the sum of the digits of a given number.
assert sum_digits(123) == 6
"""

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_digits(123))

def sum_digits(num):
    sum = 0
    for i in str(num):