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
    25
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    25
    >>> sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    120
    """
    return sum(lst[i] for i in range(len(lst)) if lst[i] % 2 == 0 and i % 2 == 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()