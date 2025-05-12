"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""


def is_num_decagonal(n):
    """
    >>> is_num_decagonal(3)
    True
    >>> is_num_decagonal(4)
    False
    """
    return n * (n + 1) == 2 * (n * (n + 1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()