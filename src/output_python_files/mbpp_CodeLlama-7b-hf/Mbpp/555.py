"""
Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.
assert difference(3) == 30
"""


def difference(n):
    """
    >>> difference(3)
    30
    >>> difference(4)
    54
    >>> difference(5)
    75
    >>> difference(6)
    91
    >>> difference(7)
    110
    >>> difference(8)
    127
    >>> difference(9)
    144
    >>> difference(10)
    161
    >>> difference(11)
    178
    >>> difference(12)
    195
    >>> difference(13)
    212
    >>> difference(14)
    229
    >>> difference(15)
    246
    >>> difference(16)
    263
    >>> difference(17)
    280
    >>> difference(18)
    297
    >>> difference(19)
    314
    >>> difference(20)
    331
    """
    return sum(range(n))**2 - sum(range(n))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
