"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""


def sum_in_range(l, r):
    """
    >>> sum_in_range(2,5)
    8
    >>> sum_in_range(1,10)
    25
    >>> sum_in_range(1,100)
    2500
    """
    return sum(range(l, r+1, 2))


if __name__ == '__main__':
    import doctest
    doctest.testmod()