"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""

def check_tuplex(tuplex, element):
    return element in tuplex

assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'z')==False
/python/python_basics/python_basics_001.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_list([1,2,3,4])==10
"""

def sum_list(listx):
    return sum(listx)

assert sum_list([1,2,3,4])==10
/python/python_basics/python_basics_003.py
"""
Write a function that takes a list and returns a new list with unique elements of the first list.
assert unique_list([1,2,3,3,3,3,4,5])==[1,2,3,4,5]
"""

def unique_list(listx):
    return list(set(listx))

assert unique_list([1,2,3,3,3,3,4,5])==[1,2,3,4,5]
/python/python_basics/python_basics_002.py
"""
Write a function that takes a list and returns a new list with only odd numbers of the first list.
assert odd_list([1,2,3,4,5,6,7])==[1,3,5,7]
"""

def odd_list(listx):
    return [x for x in listx if x%2!=0]

assert odd_list([1,2,3,4,5,6,7])==[1,3,5,7]
/python/python_basics/python_basics_004.py
"""
Write a function that takes a number and returns a list of its digits.
assert digit_list(12345)==[1,2,3,4,5]
"""

def digit_list(number):
    return [int(x) for x in str(number)]

assert digit_list(12345)==[1,2,3,4,5]
/python/python_basics/python_basics_005.py
"""
Write a function that takes a list and returns a new list with only the even elements of the first list.
assert even_list([1,2,3,4,5,6,7])==[2,4,6]
"""

def even_list(listx):
    return [x for x in listx if x%2==0]

assert even_list([1,2,3,4,5,6,7])==[2,4,6]
/python/python_basics/python_basics_006.py
"""
Write a function that takes a list and returns a new list with the square of each element.
assert square_list([1,2,3,4,5])==[1,4,9,16,25]
"""

def square_list(listx):
    return [x**2 for x in listx]

assert square_list([1,2,3,4,5])==[1,4,9,16,25]
/python/python_basics/python_basics_007.py
"""
Write a function that takes a list and returns a new list with the square of each odd number of the first list.
assert odd_square_list([1,2,3,4,5])==[1,9]
"""

def odd_square_list(listx):
    return [x**2 for x in listx if x%2!=0]

assert odd_square_list([1,2,3,4,5])==[1,9]