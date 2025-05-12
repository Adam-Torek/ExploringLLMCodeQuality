"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""

def odd_values_string(string):
    return string[::2]

print(odd_values_string('abcdef'))
/python_basics/python_basics_1.py
"""
Write a python function to find the maximum of three numbers.
assert max_of_three(1, 2, 3) == 3
"""

def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max_of_three(1, 2, 3))
/python_basics/python_basics_10.py
"""
Write a python function to find the sum of the series 1 + 1/2 + 1/3 + 1/4 +... + 1/n
assert sum_series(5) == 3.55
"""

def sum_series(n):
    return sum([1/i for i in range(1, n+1)])

print(sum_series(5))
/python_basics/python_basics_11.py
"""
Write a python function to find the sum of the series 1 - 1/2 + 1/3 - 1/4 +... + (-1)**n/n
assert sum_series(5) == 1.64
"""

def sum_series(n):
    return sum([(-1)**i/i for i in range(1, n+1)])

print(sum_series(5))
/python_basics/python_basics_12.py
"""
Write a python function to find the sum of the series 1 + 2 + 3 +... + n
assert sum_series(5) == 15
"""

def sum_series(n):
    return sum([i for i in range(1, n+1)])

print(sum_series(5))
/python_basics/python_basics_13.py
"""
Write a python function to find the sum of the series 1 + 1/2 + 1/3 +... + 1/n
assert sum_series(5) == 3.55
"""

def sum_series(n):
    return sum([1/i for i in range(1, n+1)])

print(sum_series(5))
/python_basics/python_basics_14.py
"""
Write a python function to find the sum of the series 1 - 1/2 + 1/3 - 1/4 +... + (-1)**n/n
assert sum_series(5) == 1.64
"""

def sum_series(n):
    return sum([(-1)**i/i for i in range(1, n+1)])

print(sum_series(5))
/python_basics/python_basics_15.py
"""
Write a python function to find the sum of the series 1 + 2 + 3 +... + n
assert sum_series(5) == 15
"""

def sum_series(n):
    return sum([i for i in range(1, n+1)])

print(sum_series(5))
/python_basics/python_basics_16.py
"""
Write a python function to find the sum of the series 1 + 1/2 + 1/3 +... + 1/n
assert sum_series(5) == 3.55
"""

def sum_series(n):
    return sum([1/i for i in range(1, n+1)])

print(sum_series(5))
/python_basics/python_basics_17.py
"""
Write a python function to find the sum of the series 1 - 1/2 + 1/3 - 1/4 +... + (-1)**n/n
assert sum_series(5) == 1.64
"""

def sum_series(n):
    return sum([(-1)**i/i for i in range(1, n+1)])

print(sum_series(5))
/python_basics/python_basics_18.py
"""
Write a python function