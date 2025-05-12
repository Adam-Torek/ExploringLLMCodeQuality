"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r','s']
"""

def extract_rear(tup):
    return [x[-1] for x in tup]

print(extract_rear(('Mers', 'for', 'Vers')))
/python/python_fundamentals/fundamentals/fundamentals_01.py
"""
Write a function that takes a list and returns a new list with only the first and last elements of the given list.

Example:

first_last([2, 3, 4, 5, 6]) returns [2, 6]
first_last([80, 90, 100, 110, 120]) returns [80, 120]
first_last(['hello', 'world']) returns ['hello', 'world']
"""

def first_last(list):
    return [list[0], list[-1]]

print(first_last([2, 3, 4, 5, 6]))
print(first_last([80, 90, 100, 110, 120]))
print(first_last(['hello', 'world']))
/python/python_fundamentals/fundamentals/fundamentals_03.py
"""
Write a function that takes a list and returns a new list with the first element of each string in the given list.

Example:

first_element(['hello', 'world','my', 'name', 'is', 'Anna']) returns ['h', 'w','m', 'n', 'i', 'A']
"""

def first_element(list):
    return [x[0] for x in list]

print(first_element(['hello', 'world','my', 'name', 'is', 'Anna']))
/python/python_fundamentals/fundamentals/fundamentals_02.py
"""
Write a function that takes a list and returns a new list with the last element of each string in the given list.

Example:

last_element(['hello', 'world','my', 'name', 'is', 'Anna']) returns ['o', 'd', 'y', 'e','s', 'n']
"""

def last_element(list):
    return [x[-1] for x in list]

print(last_element(['hello', 'world','my', 'name', 'is', 'Anna']))
/python/python_fundamentals/fundamentals/fundamentals_04.py
"""
Write a function that takes a list and returns a new list with the last element of each string in the given list.

Example:

last_element(['hello', 'world','my', 'name', 'is', 'Anna']) returns ['o', 'd', 'y', 'e','s', 'n']
"""

def last_element(list):
    return [x[-1] for x in list]

print(last_element(['hello', 'world','my', 'name', 'is', 'Anna']))
/python/python_fundamentals/fundamentals/fundamentals_05.py
"""
Write a function that takes a list and returns a new list with the last element of each string in the given list.

Example:

last_element(['hello', 'world','my', 'name', 'is', 'Anna']) returns ['o', 'd', 'y', 'e','s', 'n']
"""

def last_element(list):
    return [x[-1] for x in list]

print(last_element(['hello', 'world','my', 'name', 'is', 'Anna']))
/python/python_fundamentals/fundamentals/fundamentals_06.py
"""
Write a function that takes a list and returns a new list with the last element of each string in the given list.

Example:

last_element(['hello', 'world','my', 'name', 'is', 'Anna']) returns ['o', 'd', 'y', 'e','s', 'n']
"""

def last_element(list):
    return [x[-1] for x in list]

print(last_element(['hello', 'world','my', 'name', 'is', 'Anna']))
/python/python