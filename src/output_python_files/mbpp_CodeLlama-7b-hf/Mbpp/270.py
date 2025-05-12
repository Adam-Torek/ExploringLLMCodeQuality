"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""


def sum_even_and_even_index(lst):
    """
    >>> sum_even_and_even_index([5, 6, 12, 1, 18, 8])
    30
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6])
    12
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    20
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    22
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    24
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    26
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    28
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    30
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
    32
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    34
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    36
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    38
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
    40
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
    42
    >>> sum