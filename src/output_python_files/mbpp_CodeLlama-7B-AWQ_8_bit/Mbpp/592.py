"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""


def sum_Of_product(n):
    """
    >>> sum_Of_product(3)
    15
    >>> sum_Of_product(4)
    30
    >>> sum_Of_product(5)
    45
    >>> sum_Of_product(6)
    60
    >>> sum_Of_product(7)
    75
    >>> sum_Of_product(8)
    90
    >>> sum_Of_product(9)
    105
    >>> sum_Of_product(10)
    120
    """
    return sum(binomial_coefficient(i, j) for i in range(n) for j in range(i + 1))


def binomial_coefficient(n, k):
    """
    >>> binomial_coefficient(3, 2)
    3
    >>> binomial_coefficient(3, 1)
    3
    >>> binomial_coefficient(3, 0)
    1
    >>> binomial_coefficient(4, 3)
    4
    >>> binomial_coefficient(4, 2)
    6
    >>> binomial_coefficient(4, 1)
    4
    >>> binomial_coefficient(4, 0)
    1
    >>> binomial_coefficient(5, 4)
    5
    >>> binomial_coefficient(5, 3)
    10
    >>> binomial_coefficient(5, 2)
    10
    >>> binomial_coefficient(5, 1)
    5
    >>> binomial_coefficient(5, 0)
    1
    >>> binomial_coefficient(6, 5)
    6
    >>> binomial_coefficient(6, 4)
    15
    >>> binomial_coefficient(6, 3)
    20
    >>> binomial_coefficient(6, 2)
    15
    >>> binomial_coefficient(6, 1)
    6
    >>> binomial_coefficient(6, 0)
    1
    >>> binomial_coefficient(7, 6)
    7
    >>> binomial_coefficient(7, 5)
    21
    >>> binomial_coefficient(7, 4)
    35
    >>> binomial_coefficient(7, 3)
    35
    >>> binomial_coefficient(7, 2)
    21
    >>> binomial_coefficient(7, 1)
    7
    >>> binomial_coefficient(7, 0)
    1
    >>> binomial_coefficient(8, 7)
    8
    >>> binomial_coefficient(8, 6)
    28
    >>> binomial_coefficient(8, 5)
    42
    >>> binomial_coefficient(8, 4)
    56
    >>> binomial_coefficient(8, 3)
    56
    >>> binomial_coefficient(8, 2)
    42
    >>> binomial_coefficient(8, 1)
    8
    >>> binomial_coefficient(8, 0)
    1
    >>> binomial_coefficient(9, 8)
    9
    >>> binomial_coefficient(9, 7)
    36
    >>> binomial_coefficient(9, 6)
    63
    >>> binomial_coefficient(9, 5)
    90
    >>> binomial_coefficient(9, 4)
    126
    >>> binomial_coefficient(9, 3)
    126
    >>> binomial_coefficient(9, 2)
    90
    >>> binomial_coefficient(9, 1)
    36
    >>> binomial_coefficient(9, 0)
    1
    >>> binomial_coefficient(10, 9)
    10
    >>> binomial_coefficient(10, 8)
    45
    >>> binomial_coefficient(10, 7)
    84