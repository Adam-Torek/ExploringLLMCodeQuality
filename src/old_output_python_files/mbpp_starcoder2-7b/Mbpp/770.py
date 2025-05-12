"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""

def odd_num_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**4
    return sum

print(odd_num_sum(2))
<file_sep>/python/python_basics/python_basics_1.py
"""
Write a python function to find the sum of first n natural numbers.
assert sum_of_n(2) == 3
"""

def sum_of_n(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

print(sum_of_n(2))
<file_sep>/python/python_basics/python_basics_3.py
"""
Write a python function to find the sum of squares of first n natural numbers.
assert sum_of_squares(2) == 5
"""

def sum_of_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum

print(sum_of_squares(2))
<file_sep>/python/python_basics/python_basics_2.py
"""
Write a python function to find the sum of cubes of first n natural numbers.
assert sum_of_cubes(2) == 14
"""

def sum_of_cubes(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**3
    return sum

print(sum_of_cubes(2))
<|endoftext|>