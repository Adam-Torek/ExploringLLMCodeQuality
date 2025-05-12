"""
Write a function to merge three dictionaries into a single dictionary.
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""

def merge_dictionaries_three(dict1, dict2, dict3):
    dict1.update(dict2)
    dict1.update(dict3)
    return dict1

print(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }))
<file_sep>/python_basics/python_basics_1.py
"""
Write a function to calculate the sum of three given numbers.
assert sum_three(1,2,3)==6
"""

def sum_three(a,b,c):
    return a+b+c

print(sum_three(1,2,3))
<file_sep>/python_basics/python_basics_10.py
"""
Write a function to check whether a given number is in a given range.
assert number_range(1, 1, 10)==True
assert number_range(-1, 0, 10)==True
assert number_range(10, 1, 10)==False
"""

def number_range(number, start, end):
    if number >= start and number <= end:
        return True
    else:
        return False

print(number_range(1, 1, 10))
print(number_range(-1, 0, 10))
print(number_range(10, 1, 10))
<file_sep>/python_basics/python_basics_12.py
"""
Write a function to check whether a given number is in a given range inclusively.
assert number_range_inclusive(1, 1, 10)==True
assert number_range_inclusive(-1, 0, 10)==True
assert number_range_inclusive(10, 1, 10)==True
"""

def number_range_inclusive(number, start, end):
    if number >= start and number <= end:
        return True
    else:
        return False

print(number_range_inclusive(1, 1, 10))
print(number_range_inclusive(-1, 0, 10))
print(number_range_inclusive(10, 1, 10))
<file_sep>/python_basics/python_basics_13.py
"""
Write a function to create a dictionary with (i, i*i) as the key-value pair.
assert square_dict(5)=={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

def square_dict(n):
    dict = {}
    for i in range(1, n+1):
        dict[i] = i*i
    return dict

print(square_dict(5))
<file_sep>/python_basics/python_basics_14.py
"""
Write a function to create a dictionary with (i, i**3) as the key-value pair.
assert cube_dict(5)=={1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
"""

def cube_dict(n):
    dict = {}
    for i in range(1, n+1):
        dict[i] = i**3
    return dict

print(cube_dict(5))
<file_sep>/python_basics/python_basics_15.py
"""
Write a function to create a dictionary with (i, i**8) as the key-value pair.
assert eight_dict(5)=={1: 1, 2: 256, 3: 6561, 4: 16777216, 5: 4294967296}
"""

def eight_dict(n):
    dict = {}
    for