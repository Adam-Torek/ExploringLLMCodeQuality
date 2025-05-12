"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""

def unique_product(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    product = 1
    for i in unique_list:
        product *= i
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))
/python_basics/python_basics_1.py
"""
Write a python function to calculate the sum of the digits of a given number.
assert sum_digits(123) == 6
"""

def sum_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

print(sum_digits(123))
/python_basics/python_basics_3.py
"""
Write a python function to calculate the sum of the digits of a given number.
assert sum_digits(123) == 6
"""

def sum_digits(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum

print(sum_digits(123))
/python_basics/python_basics_2.py
"""
Write a python function to calculate the sum of the digits of a given number.
assert sum_digits(123) == 6
"""

def sum_digits(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum

print(sum_digits(123))