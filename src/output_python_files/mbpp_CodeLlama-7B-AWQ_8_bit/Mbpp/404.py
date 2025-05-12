"""
Write a python function to find the minimum of two numbers.
assert minimum(1,2) == 1
"""


def minimum(a, b):
    """
    >>> minimum(1,2)
    1
    >>> minimum(2,1)
    1
    >>> minimum(1,1)
    1
    """
    return min(a, b)


if __name__ == "__main__":
    import doctest

    doctest.testmod()