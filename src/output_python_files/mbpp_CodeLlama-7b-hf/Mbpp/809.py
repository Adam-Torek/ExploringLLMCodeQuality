"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""


def check_smaller(t1, t2):
    """
    >>> check_smaller((1, 2, 3), (2, 3, 4))
    False
    >>> check_smaller((1, 2, 3), (2, 3, 3))
    True
    >>> check_smaller((1, 2, 3), (2, 3, 2))
    False
    >>> check_smaller((1, 2, 3), (2, 3, 1))
    False
    >>> check_smaller((1, 2, 3), (2, 2, 3))
    False
    >>> check_smaller((1, 2, 3), (2, 2, 2))
    False
    >>> check_smaller((1, 2, 3), (2, 2, 1))
    False
    >>> check_smaller((1, 2, 3), (1, 2, 3))
    False
    >>> check_smaller((1, 2, 3), (1, 2, 2))
    False
    >>> check_smaller((1, 2, 3), (1, 2, 1))
    False
    >>> check_smaller((1, 2, 3), (1, 1, 3))
    False
    >>> check_smaller((1, 2, 3), (1, 1, 2))
    False
    >>> check_smaller((1, 2, 3), (1, 1, 1))
    False
    >>> check_smaller((1, 2, 3), (1, 0, 3))
    False
    >>> check_smaller((1, 2, 3), (1, 0, 2))
    False
    >>> check_smaller((1, 2, 3), (1, 0, 1))
    False
    >>> check_smaller((1, 2, 3), (0, 2, 3))
    False
    >>> check_smaller((1, 2, 3), (0, 2, 2))
    False
    >>> check_smaller((1, 2, 3), (0, 2, 1))
    False
    >>> check_smaller((1, 2, 3), (0, 1, 3))
    False
    >>> check_smaller((1, 2, 3), (0, 1, 2))
    False
    >>> check_smaller((1, 2, 3), (0, 1, 1))
    False
    >>> check_smaller((1, 2, 3), (0, 0, 3))
    False
    >>> check_smaller((1, 2, 3), (0, 0, 2))
    False
    >>> check_smaller((1, 2, 3), (0, 0, 1))
    False
    """
    if len(t1) != len(t2):
        return False
    for i in range(len(t1)):
        if t1[i] > t2[i]:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()