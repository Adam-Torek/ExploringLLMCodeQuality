"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""


def set_left_most_unset_bit(n):
    """
    >>> set_left_most_unset_bit(10)
    14
    """
    return n | (n + 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()