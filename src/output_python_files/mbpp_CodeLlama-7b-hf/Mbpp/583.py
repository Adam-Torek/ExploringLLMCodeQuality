"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""


def catalan_number(n):
    """
    >>> catalan_number(10)
    16796
    """
    if n == 0:
        return 1
    else:
        return (2 * n - 1) * catalan_number(n - 1) / n


if __name__ == "__main__":
    import doctest

    doctest.testmod()