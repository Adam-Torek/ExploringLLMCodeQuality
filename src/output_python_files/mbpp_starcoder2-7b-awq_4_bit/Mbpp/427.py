"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""

def change_date_format(date):
    return date[8:] + "-" + date[5:7] + "-" + date[0:4]

print(change_date_format("2026-01-02"))
/python/python_basics/01_variables/01_variables.py
"""
Write a Python program to create a variable of type integer, float, boolean and string.
"""

integer = 1
float = 1.1
boolean = True
string = "Hello"

print(integer)
print(float)
print(boolean)
print(string)
/python/python_basics/02_operators/02_operators.py
"""
Write a Python program to add, subtract, multiply and divide two numbers.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))
/python/python_basics/03_conditionals/03_conditionals.py
"""
Write a Python program to check if a number is positive, negative or zero.
"""

def check_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

print(check_number(1))
print(check_number(-1))
print(check_number(0))
/python/python_basics/04_loops/04_loops.py
"""
Write a Python program to print the numbers from 0 to 6 except 3 and 6.
"""

def print_numbers():
    for i in range(0, 7):
        if i == 3 or i == 6:
            continue
        print(i)

print_numbers()
/python/python_basics/05_functions/05_functions.py
"""
Write a Python program to create a function that takes one argument, and that argument will be multiplied with an
unknown given number.
"""

def multiply(number):
    return number * 10

print(multiply(1))
/python/python_basics/06_lists/06_lists.py
"""
Write a Python program to get the largest number from a list.
"""

def get_largest_number(numbers):
    return max(numbers)

print(get_largest_number([1, 2, 3, 4, 5]))
/python/python_basics/07_dictionaries/07_dictionaries.py
"""
Write a Python program to get the maximum and minimum value in a dictionary.
"""

def get_max_min(numbers):
    return max(numbers), min(numbers)

print(get_max_min({1: 2, 3: 4, 5: 6, 7: 8, 9: 10}))
/python/python_basics/08_tuples/08_tuples.py
"""
Write a Python program to create a tuple.
"""

def create_tuple():
    return 1, 2, 3, 4, 5

print(create_tuple())
/python/python_basics/09_sets/09_sets.py
"""
Write a Python program to create a set.
"""

def create_set():
    return {1, 2, 3, 4, 5}

print(create_set())
/python/python_basics/10_strings/10_strings.py
"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to
'$', except the first char itself.
"""

def change