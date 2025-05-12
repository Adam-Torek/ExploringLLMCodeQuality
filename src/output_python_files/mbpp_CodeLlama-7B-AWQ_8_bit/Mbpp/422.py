"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""


def find_Average_Of_Cube(n):
    """
    >>> find_Average_Of_Cube(2)
    4.5
    >>> find_Average_Of_Cube(3)
    6.0
    >>> find_Average_Of_Cube(4)
    7.0
    >>> find_Average_Of_Cube(5)
    7.666666666666667
    >>> find_Average_Of_Cube(6)
    8.0
    >>> find_Average_Of_Cube(7)
    8.666666666666667
    >>> find_Average_Of_Cube(8)
    9.0
    >>> find_Average_Of_Cube(9)
    9.666666666666667
    >>> find_Average_Of_Cube(10)
    10.0
    >>> find_Average_Of_Cube(11)
    10.666666666666666
    >>> find_Average_Of_Cube(12)
    11.0
    >>> find_Average_Of_Cube(13)
    11.666666666666667
    >>> find_Average_Of_Cube(14)
    12.0
    >>> find_Average_Of_Cube(15)
    12.666666666666667
    >>> find_Average_Of_Cube(16)
    13.0
    >>> find_Average_Of_Cube(17)
    13.666666666666667
    >>> find_Average_Of_Cube(18)
    14.0
    >>> find_Average_Of_Cube(19)
    14.666666666666667
    >>> find_Average_Of_Cube(20)
    15.0
    """
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum/n


if __name__ == '__main__':
    import doctest
    doctest.testmod()