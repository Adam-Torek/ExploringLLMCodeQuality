"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""


def max_val(lst):
    """
    >>> max_val(['Python', 3, 2, 4, 5, 'version'])
    5
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    10
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello'])
    10
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello', 11])
    11
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello', 11, 12])
    12
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello', 11, 12, 13])
    13
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello', 11, 12, 13, 14])
    14
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello', 11, 12, 13, 14, 15])
    15
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello', 11, 12, 13, 14, 15, 16])
    16
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello', 11, 12, 13, 14, 15, 16, 17])
    17
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello', 11, 12, 13, 14, 15, 16, 17, 18])
    18
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello', 11, 12, 13, 14, 15, 16, 17, 18, 19])
    19
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello', 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    20
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello', 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
    21
    >>> max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello', 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
    22
    >>> max_val([1, 2,