"""
Write a python function to find the maximum of two numbers.
assert maximum(5,10) == 10
"""


def maximum(a, b):
    """
    >>> maximum(5,10)
    10
    >>> maximum(10,5)
    10
    >>> maximum(5,5)
    5
    """
    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':
    import doctest
    doctest.testmod()