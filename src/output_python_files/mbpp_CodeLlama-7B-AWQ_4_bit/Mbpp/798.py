"""
Write a python function to find the sum of an array.
assert _sum([1, 2, 3]) == 6
"""


def _sum(arr):
    """
    >>> _sum([1, 2, 3])
    6
    >>> _sum([1, 2, 3, 4, 5])
    15
    >>> _sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    55
    """
    return sum(arr)


if __name__ == "__main__":
    import doctest

    doctest.testmod()