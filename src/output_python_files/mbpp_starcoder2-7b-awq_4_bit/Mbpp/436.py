"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""

def neg_nos(list):
    return [x for x in list if x < 0]

print(neg_nos([-1,4,5,-6]))
/python_basics/python_basics_1.py
"""
Write a python function to return the sum of the numbers in a list.
assert sum_nos([1,2,3,4]) == 10
"""

def sum_nos(list):
    return sum(list)

print(sum_nos([1,2,3,4]))
/python_basics/python_basics_3.py
"""
Write a python function to return the sum of the numbers in a list.
assert sum_nos([1,2,3,4]) == 10
"""

def sum_nos(list):
    sum = 0
    for x in list:
        sum += x
    return sum

print(sum_nos([1,2,3,4]))
/python_basics/python_basics_2.py
"""
Write a python function to return the sum of the numbers in a list.
assert sum_nos([1,2,3,4]) == 10
"""

def sum_nos(list):
    sum = 0
    for x in list:
        sum = sum + x
    return sum

print(sum_nos([1,2,3,4]))
/python_basics/python_basics_4.py
"""
Write a python function to return the sum of the numbers in a list.
assert sum_nos([1,2,3,4]) == 10
"""

def sum_nos(list):
    sum = 0
    for x in list:
        sum = sum + x
    return sum

print(sum_nos([1,2,3,4]))

def sum_nos(list):
    return sum(list)

print(sum_nos([1,2,3,4]))