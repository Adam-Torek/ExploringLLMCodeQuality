"""
Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""

def dict_filter(dictionary,n):
    new_dict = {}
    for key,value in dictionary.items():
        if value >= n:
            new_dict[key] = value
    return new_dict

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170))
<file_sep>/python_practice/python_practice_2/python_practice_2_1.py
"""
Write a function that takes in a list of numbers and returns the largest number in the list.
assert largest_number([1,2,3,4,5])==5
"""

def largest_number(list_of_numbers):
    largest_number = list_of_numbers[0]
    for number in list_of_numbers:
        if number > largest_number:
            largest_number = number
    return largest_number

print(largest_number([1,2,3,4,5]))
<file_sep>/python_practice/python_practice_1/python_practice_1_1.py
"""
Write a function that takes in a list of numbers and returns the smallest number in the list.
assert smallest_number([1,2,3,4,5])==1
"""

def smallest_number(list_of_numbers):
    smallest_number = list_of_numbers[0]
    for number in list_of_numbers:
        if number < smallest_number:
            smallest_number = number
    return smallest_number

print(smallest_number([1,2,3,4,5]))
<file_sep>/python_practice/python_practice_2/python_practice_2_2.py
"""
Write a function that takes in a list of numbers and returns the smallest number in the list.
assert smallest_number([1,2,3,4,5])==1
"""

def smallest_number(list_of_numbers):
    smallest_number = list_of_numbers[0]
    for number in list_of_numbers:
        if number < smallest_number:
            smallest_number = number
    return smallest_number

print(smallest_number([1,2,3,4,5]))
<file_sep>/python_practice/python_practice_1/python_practice_1_2.py
"""
Write a function that takes in a list of numbers and returns the smallest number in the list.
assert smallest_number([1,2,3,4,5])==1
"""

def smallest_number(list_of_numbers):
    smallest_number = list_of_numbers[0]
    for number in list_of_numbers:
        if number < smallest_number:
            smallest_number = number
    return smallest_number

print(smallest_number([1,2,3,4,5]))
<file_sep>/python_practice/python_practice_2/python_practice_2_3.py
"""
Write a function that takes in a list of numbers and returns the smallest number in the list.
assert smallest_number([1,2,3,4,5])==1
"""

def smallest_number(list_of_numbers):
    smallest_number = list_of_numbers[0]
    for number in list_of_numbers:
        if number < smallest_number:
            smallest_number = number
    return smallest_number

print(smallest_number([1,2,3,4,5]))
<file_sep>/python_practice/python_practice_1/python_practice_1_3.py
"""
Write a function that takes in a list of numbers and returns the smallest number in the list.
assert smallest_number([1,2,3,4,5])==1
"""

def smallest_number(list_of_numbers):
    smallest_number = list_of_numbers[0]
    for number in list_of_numbers:
        if number