"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""

def tuple_intersection(tuple_list):
    return set.intersection(*tuple_list)

print(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]))
<file_sep>/python/python_basics/python_basics_001.py
"""
Write a function to find the sum of the first n natural numbers.
assert sum_of_n(10) == 55
"""

def sum_of_n(n):
    return n * (n + 1) / 2

print(sum_of_n(10))
<file_sep>/python/python_basics/python_basics_004.py
"""
Write a function to find the factorial of a number.
assert factorial(5) == 120
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
<file_sep>/python/python_basics/python_basics_003.py
"""
Write a function to find the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    return sum(int(x) for x in str(n))

print(sum_of_digits(123))
<file_sep>/python/python_basics/python_basics_002.py
"""
Write a function to find the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    return sum(int(x) for x in str(n))

print(sum_of_digits(123))
<file_sep>/python/python_basics/python_basics_005.py
"""
Write a function to find the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    return sum(int(x) for x in str(n))

print(sum_of_digits(123))
<file_sep>/python/python_basics/python_basics_006.py
"""
Write a function to find the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    return sum(int(x) for x in str(n))

print(sum_of_digits(123))
<file_sep>/python/python_basics/python_basics_007.py
"""
Write a function to find the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    return sum(int(x) for x in str(n))

print(sum_of_digits(123))
<file_sep>/python/python_basics/python_basics_008.py
"""
Write a function to find the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    return sum(int(x) for x in str(n))

print(sum_of_digits(123))
<file_sep>/python/python_basics/python_basics_009.py
"""
Write a function to find the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    return sum(int(x) for x in str(n))

print(sum_of_digits(123))
<file_sep>/python/python_basics/python_basics_010.py
"""