"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""


def check_distinct(tup):
    """
    >>> check_distinct((1, 4, 5, 6, 1, 4))
    False
    >>> check_distinct((1, 4, 5, 6, 1, 4, 7))
    True
    >>> check_distinct((1, 4, 5, 6, 1, 4, 7, 8))
    False
    """
    return len(tup) == len(set(tup))


if __name__ == "__main__":
    import doctest

    doctest.testmod()