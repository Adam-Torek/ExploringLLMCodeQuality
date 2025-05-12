"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""

def intersection_array(a,b):
    return list(set(a).intersection(set(b)))

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]))
/python/python_basics/python_basics_1.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
"""

def largest_number(numbers):
    return max(numbers)

print(largest_number([1,2,3,4,5,6,7,8,9,10]))
/python/python_basics/python_basics_3.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
"""

def smallest_number(numbers):
    return min(numbers)

print(smallest_number([1,2,3,4,5,6,7,8,9,10]))
/python/python_basics/python_basics_2.py
"""
Write a function that takes a list of numbers and returns the second largest number in the list.
"""

def second_largest_number(numbers):
    return sorted(numbers)[-2]

print(second_largest_number([1,2,3,4,5,6,7,8,9,10]))
/python/python_basics/python_basics_4.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
"""

def second_smallest_number(numbers):
    return sorted(numbers)[1]

print(second_smallest_number([1,2,3,4,5,6,7,8,9,10]))
/python/python_basics/python_basics_5.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
"""

def second_smallest_number(numbers):
    return sorted(numbers)[1]

print(second_smallest_number([1,2,3,4,5,6,7,8,9,10]))
/python/python_basics/python_basics_6.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
"""

def second_smallest_number(numbers):
    return sorted(numbers)[1]

print(second_smallest_number([1,2,3,4,5,6,7,8,9,10]))