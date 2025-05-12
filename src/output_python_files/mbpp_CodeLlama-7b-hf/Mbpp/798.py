"""
Write a python function to find the sum of an array.
assert _sum([1, 2, 3]) == 6
"""


def _sum(arr):
    """
    >>> _sum([1, 2, 3])
    6
    """
    return sum(arr)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
