"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""


def cube_Sum(n):
    """
    >>> cube_Sum(2)
    72
    >>> cube_Sum(3)
    1728
    >>> cube_Sum(4)
    3744
    >>> cube_Sum(5)
    6120
    >>> cube_Sum(6)
    9216
    >>> cube_Sum(7)
    12344
    >>> cube_Sum(8)
    15625
    >>> cube_Sum(9)
    19024
    >>> cube_Sum(10)
    22524
    >>> cube_Sum(11)
    25925
    >>> cube_Sum(12)
    29424
    >>> cube_Sum(13)
    32924
    >>> cube_Sum(14)
    36424
    >>> cube_Sum(15)
    40024
    >>> cube_Sum(16)
    43624
    >>> cube_Sum(17)
    47224
    >>> cube_Sum(18)
    50824
    >>> cube_Sum(19)
    54424
    >>> cube_Sum(20)
    58024
    """
    return sum(i**3 for i in range(2, n+1) if i % 2 == 0)


if __name__ == "__main__":
    import doctest
    doctest.testmod()