"""
Write a function to rotate a given list by specified number of items to the right direction. https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""
def rotate_right(lst,n):
    return lst[n:]+lst[:n]

assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

"""
Write a function to rotate a given list by specified number of items to the left direction. https://www.geeksforgeeks.org/python-program-to-left-rotate-a-list-by-n-places/
assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
"""
def rotate_left(lst,n):
    return lst[-n:]+lst[:-n]

assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[4, 5, 6, 7, 8, 9, 10, 1, 2, 3]

"""
Write a function to reverse a given list. https://www.geeksforgeeks.org/python-program-to-reverse-a-list/
assert reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
"""
def reverse(lst):
    return lst[::-1]

assert reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

"""
Write a function to reverse a given list. https://www.geeksforgeeks.org/python-program-to-reverse-a-list/
assert reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
"""
def reverse(lst):
    return lst[::-1]

assert reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

"""
Write a function to reverse a given list. https://www.geeksforgeeks.org/python-program-to-reverse-a-list/
assert reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
"""
def reverse(lst):
    return lst[::-1]

assert reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

"""
Write a function to reverse a given list. https://www.geeksforgeeks.org/python-program-to-reverse-a-list/
assert reverse([1, 2, 3, 4,