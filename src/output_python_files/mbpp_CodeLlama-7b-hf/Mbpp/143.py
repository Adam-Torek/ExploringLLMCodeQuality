"""
Write a function to find number of lists present in the given tuple.
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
"""


def find_lists(tup):
    """
    >>> find_lists(([1, 2, 3, 4], [5, 6, 7, 8]))
    2
    >>> find_lists(([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]))
    3
    >>> find_lists(([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]))
    4
    """
    return len([x for x in tup if isinstance(x, list)])


if __name__ == "__main__":
    import doctest

    doctest.testmod()