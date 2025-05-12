"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""


def sum_series(n):
    """
    >>> sum_series(6)
    12
    >>> sum_series(10)
    30
    >>> sum_series(100)
    2500
    """
    return sum(range(n, 0, -2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()