"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""

def odd_num_sum(n):
    return sum([i**4 for i in range(1,n+1) if i%2!=0])

print(odd_num_sum(2))
/python_basics/python_basics_1.py
"""
Write a python function to find the sum of first n natural numbers.
assert sum_of_n(2) == 3
"""

def sum_of_n(n):
    return sum(range(1,n+1))

print(sum_of_n(2))
/python_basics/python_basics_2.py
"""
Write a python function to find the sum of squares of first n natural numbers.
assert sum_of_squares(2) == 5
"""

def sum_of_squares(n):
    return sum([i**2 for i in range(1,n+1)])

print(sum_of_squares(2))
/python_basics/python_basics_3.py
"""
Write a python function to find the sum of cubes of first n natural numbers.
assert sum_of_cubes(2) == 9
"""

def sum_of_cubes(n):
    return sum([i**3 for i in range(1,n+1)])

print(sum_of_cubes(2))