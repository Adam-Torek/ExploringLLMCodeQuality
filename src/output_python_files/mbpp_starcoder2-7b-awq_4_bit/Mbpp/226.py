"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""

def odd_values_string(string):
    return string[::2]

print(odd_values_string('abcdef'))
/python/python_basics/python_basics_001.py
"""
Write a python function to print the even numbers from 1 to 100.
"""

def even_numbers():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)

even_numbers()
/python/python_basics/python_basics_002.py
"""
Write a python function to print the odd numbers from 1 to 100.
"""

def odd_numbers():
    for i in range(1, 101):
        if i % 2!= 0:
            print(i)

odd_numbers()
/python/python_basics/python_basics_004.py
"""
Write a python function to print the sum of all the even numbers from 1 to 100.
"""

def even_numbers_sum():
    sum = 0
    for i in range(1, 101):
        if i % 2 == 0:
            sum += i
    print(sum)

even_numbers_sum()
/python/python_basics/python_basics_003.py
"""
Write a python function to print the sum of all the odd numbers from 1 to 100.
"""

def odd_numbers_sum():
    sum = 0
    for i in range(1, 101):
        if i % 2!= 0:
            sum += i
    print(sum)

odd_numbers_sum()
/python/python_basics/python_basics_005.py
"""
Write a python function to print the sum of all the numbers from 1 to 100.
"""

def numbers_sum():
    sum = 0
    for i in range(1, 101):
        sum += i
    print(sum)

numbers_sum()
/python/python_basics/python_basics_006.py
"""
Write a python function to print the sum of all the numbers from 1 to 100 which are divisible by 3.
"""

def numbers_divisible_by_3():
    sum = 0
    for i in range(1, 101):
        if i % 3 == 0:
            sum += i
    print(sum)

numbers_divisible_by_3()
/python/python_basics/python_basics_007.py
"""
Write a python function to print the sum of all the numbers from 1 to 100 which are divisible by 5.
"""

def numbers_divisible_by_5():
    sum = 0
    for i in range(1, 101):
        if i % 5 == 0:
            sum += i
    print(sum)

numbers_divisible_by_5()
/python/python_basics/python_basics_008.py
"""
Write a python function to print the sum of all the numbers from 1 to 100 which are divisible by 3 and 5.
"""

def numbers_divisible_by_3_and_5():
    sum = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
    print(sum)

numbers_divisible_by_3_and_5()
/python/python_basics/python_basics_009.py
"""
Write a python function to print the sum of all the numbers from 1 to 100 which are divisible by 3 or 5.
"""

def numbers_divisible_by_3_or_5():
    sum = 0
    for i