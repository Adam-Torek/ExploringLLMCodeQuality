"""
Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""

def dict_filter(dictionary, n):
    new_dict = {}
    for key in dictionary:
        if dictionary[key] >= n:
            new_dict[key] = dictionary[key]
    return new_dict

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170))
/week_01/day_03/01_list_functions.py
"""
Write a function that takes in a list and returns a new list with only the even numbers.
assert list_filter([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
"""

def list_filter(list):
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print(list_filter([1, 2, 3, 4, 5, 6]))
/week_01/day_03/02_list_functions.py
"""
Write a function that takes in a list and returns a new list with only the odd numbers.
assert list_filter([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
"""

def list_filter(list):
    new_list = []
    for i in list:
        if i % 2!= 0:
            new_list.append(i)
    return new_list

print(list_filter([1, 2, 3, 4, 5, 6]))
/week_01/day_03/03_list_functions.py
"""
Write a function that takes in a list and returns a new list with only the positive numbers.
assert list_filter([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
"""

def list_filter(list):
    new_list = []
    for i in list:
        if i > 0:
            new_list.append(i)
    return new_list

print(list_filter([1, 2, 3, 4, 5, 6]))
/week_01/day_03/04_list_functions.py
"""
Write a function that takes in a list and returns a new list with only the negative numbers.
assert list_filter([1, 2, 3, 4, 5, 6]) == [-1, -2, -3, -4, -5, -6]
"""

def list_filter(list):
    new_list = []
    for i in list:
        if i < 0:
            new_list.append(i)
    return new_list

print(list_filter([1, 2, 3, 4, 5, 6]))
/week_01/day_03/05_list_functions.py
"""
Write a function that takes in a list and returns a new list with only the multiples of 3.
assert list_filter([1, 2, 3, 4, 5, 6]) == [3, 6]
"""

def list_filter(list):
    new_list = []
    for i in list:
        if i % 3 == 0:
            new_list.append(i)
    return new_list

print(list_filter([1, 2, 3, 4, 5, 6]))
/week_01/day_03/06_list_functions.py
"""
Write a function that takes in a list and returns a new list with