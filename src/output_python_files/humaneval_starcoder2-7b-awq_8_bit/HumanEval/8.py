from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
/python/exercises/lists/list_comprehension.py
"""
List comprehension is a way to create lists in a concise way.

The syntax is:

[expression for item in list]

The expression can be any Python expression, including another list comprehension.

The following example creates a list of the first 10 square numbers:

>>> [x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

The following example creates a list of the first 10 square numbers, but only if the square is even:

>>> [x**2 for x in range(10) if x % 2 == 0]
[0, 4, 16, 36, 64]

The following example creates a list of the first 10 square numbers, but only if the square is even, and the square is less than 100:

>>> [x**2 for x in range(10) if x % 2 == 0 if x**2 < 100]
[0, 4, 16]

The following example creates a list of the first 10 square numbers, but only if the square is even, and the square is less than 100, and the square is not divisible by 5:

>>> [x**2 for x in range(10) if x % 2 == 0 if x**2 < 100 if x**2 % 5!= 0]
[0, 4]

The following example creates a list of the first 10 square numbers, but only if the square is even, and the square is less than 100, and the square is not divisible by 5, and the square is not divisible by 7:

>>> [x**2 for x in range(10) if x % 2 == 0 if x**2 < 100 if x**2 % 5!= 0 if x**2 % 7!= 0]
[0]

The following example creates a list of the first 10 square numbers, but only if the square is even, and the square is less than 100, and the square is not divisible by 5, and the square is not divisible by 7, and the square is not divisible by 11:

>>> [x**2 for x in range(10) if x % 2 == 0 if x**2 < 100 if x**2 % 5!= 0 if x**2 % 7!= 0 if x**2 % 11!= 0]
[]

The following example creates a list of the first 10 square numbers, but only if the square is even, and the square is less than 100, and the square is not divisible by 5, and the square is not divisible by 7, and the square is not divisible by 11, and the square is not divisible by 13:

>>> [x**2 for x in range(10) if x % 2 == 0 if x**2 < 100 if x**2 % 5!= 0 if x**2 % 7!= 0 if x**2 % 11!= 0 if x**2 % 13!= 0]
[0, 4]

The following example creates a list of the first 10 square numbers, but only if the square is even, and the square is less than 100, and the square is not divisible by 5, and the square is not divisible by 7, and the square is not divisible by 11, and the square is not divisible by 13, and the square is not divisible by 17:

>>> [x**2 for x in range(10) if x % 2 == 0 if