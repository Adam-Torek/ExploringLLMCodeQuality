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
    """
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()