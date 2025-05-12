"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""


def is_nonagonal(n):
    """
    >>> is_nonagonal(10)
    325
    """
    return n * (n + 1) * (2 * n + 1) // 6


if __name__ == "__main__":
    import doctest

    doctest.testmod()
