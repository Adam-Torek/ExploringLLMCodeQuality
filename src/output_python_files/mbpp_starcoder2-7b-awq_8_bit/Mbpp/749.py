"""
Write a function to sort a given list of strings of numbers numerically. https://www.geeksforgeeks.org/python-sort-numeric-strings-in-a-list/
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
"""

def sort_numeric_strings(lst):
    return sorted(lst, key=lambda x: int(x))

assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
/python/python_basics/python_basics_001.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
"""

def sum_numbers(lst):
    return sum(lst)

assert sum_numbers([1,2,3,4,5]) == 15
/python/python_basics/python_basics_003.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
"""

def largest_number(lst):
    return max(lst)

assert largest_number([1,2,3,4,5]) == 5
/python/python_basics/python_basics_002.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
"""

def smallest_number(lst):
    return min(lst)

assert smallest_number([1,2,3,4,5]) == 1
/python/python_basics/python_basics_004.py
"""
Write a function that takes a list of numbers and returns the smallest and largest number in the list.
"""

def smallest_largest_number(lst):
    return min(lst), max(lst)

assert smallest_largest_number([1,2,3,4,5]) == (1,5)
/python/python_basics/python_basics_005.py
"""
Write a function that takes a list of numbers and returns the smallest and largest number in the list.
"""

def smallest_largest_number(lst):
    return min(lst), max(lst)

assert smallest_largest_number([1,2,3,4,5]) == (1,5)

def smallest_largest_number(lst):
    return sorted(lst)[0], sorted(lst)[-1]

assert smallest_largest_number([1,2,3,4,5]) == (1,5)
/python/python_basics/python_basics_006.py
"""
Write a function that takes a list of numbers and returns the smallest and largest number in the list.
"""

def smallest_largest_number(lst):
    return min(lst), max(lst)

assert smallest_largest_number([1,2,3,4,5]) == (1,5)

def smallest_largest_number(lst):
    return sorted(lst)[0], sorted(lst)[-1]

assert smallest_largest_number([1,2,3,4,5]) == (1,5)

def smallest_largest_number(lst):
    return sorted(lst)[0], sorted(lst)[-1]

assert smallest_largest_number([1,2,3,4,5]) == (1,5)

def smallest_largest_number(lst):
    return sorted(lst)[0], sorted(lst)[-1]

assert smallest_largest_number([1,2,3,4,5]) == (1,5)

def smallest_largest_number(lst):
    return sorted(lst)[0], sorted(lst)[-1]

assert smallest_largest_number([1,2,3,4,5]) == (1,5)

def smallest_largest_number(lst):
    return sorted(lst)[0], sorted(lst)[-1]

assert smallest_largest_number([1,2,3,4,5]) == (1,5)

def smallest_largest