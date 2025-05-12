"""
Write a function to rotate a given list by specified number of items to the right direction. https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""

def rotate_right(lst,n):
    return lst[n:] + lst[:n]

assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
/python/list_comprehension.py
"""
Write a function that takes a list of numbers and returns a list of the square of each number.
"""

def square(lst):
    return [i**2 for i in lst]

assert square([1,2,3,4,5])==[1,4,9,16,25]
/python/list_of_lists.py
"""
Write a function that takes a list of numbers and returns a list of the square of each number.
"""

def square(lst):
    return [[i**2 for i in lst]]

assert square([1,2,3,4,5])==[[1,4,9,16,25]]
/python/list_of_lists_2.py
"""
Write a function that takes a list of numbers and returns a list of the square of each number.
"""

def square(lst):
    return [[i**2 for i in lst]]

assert square([1,2,3,4,5])==[[1,4,9,16,25]]

def square(lst):
    return [[i**2 for i in lst] for i in lst]

assert square([1,2,3,4,5])==[[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25]]
/python/list_of_lists_3.py
"""
Write a function that takes a list of numbers and returns a list of the square of each number.
"""

def square(lst):
    return [[i**2 for i in lst] for i in lst]

assert square([1,2,3,4,5])==[[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25]]

def square(lst):
    return [[i**2 for i in lst] for i in lst]

assert square([1,2,3,4,5])==[[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25]]

def square(lst):
    return [[i**2 for i in lst] for i in lst]

assert square([1,2,3,4,5])==[[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25]]

def square(lst):
    return [[i**2 for i in lst] for i in lst]

assert square([1,2,3,4,5])==[[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25],[1,4,9,16,25]]

def square(lst):
    return [[i**2 for i in lst] for i in lst]