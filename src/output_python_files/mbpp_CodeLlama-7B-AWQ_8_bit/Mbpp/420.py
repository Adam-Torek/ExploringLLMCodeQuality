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
    67656
    >>> cube_Sum(6)
    1089728
    """
    return sum(i**3 for i in range(2, n+1) if i % 2 == 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()