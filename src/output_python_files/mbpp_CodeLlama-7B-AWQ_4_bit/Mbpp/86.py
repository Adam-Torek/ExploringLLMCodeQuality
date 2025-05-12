"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""


def centered_hexagonal_number(n):
    """
    >>> centered_hexagonal_number(10)
    271
    """
    return (n * (2 * n - 1)) // 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()