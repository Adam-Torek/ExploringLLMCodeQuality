"""
Write a function to find the nth tetrahedral number.
assert tetrahedral_number(5) == 35
"""


def tetrahedral_number(n):
    """
    >>> tetrahedral_number(5)
    35
    """
    return (n * (n + 1)) // 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()