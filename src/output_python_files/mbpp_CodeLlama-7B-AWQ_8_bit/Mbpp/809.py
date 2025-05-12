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
    >>> check_smaller((1, 2, 3), (2, 1, 3))
    False
    >>> check_smaller((1, 2, 3), (2, 1, 2))
    False
    >>> check_smaller((1, 2, 3), (2, 1, 1))
    False
    >>> check_smaller((1, 2, 3), (1, 2, 3))
    True
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
    >>> check_smaller((1, 2, 3), (1, 2, 4))
    False
    >>> check_smaller((1, 2, 3), (1, 3, 4))
    False
    >>> check_smaller((1, 2, 3), (1, 4, 4))
    False
    >>> check_smaller((1, 2, 3), (2, 4, 4))
    False
    >>> check_smaller((1, 2, 3), (3, 4, 4))
    False
    >>> check_smaller((1, 2, 3), (4, 4, 4))
    False
    >>> check_smaller((1, 2, 3), (4, 3, 4))
    False
    >>> check_smaller((1, 2, 3), (4, 2, 4))
    False
    >>> check_smaller((1, 2, 3), (4, 1, 4))
    False
    >>> check_smaller((1, 2, 3), (4, 4, 3))
    False
    >>> check_smaller((1, 2, 3), (4, 4, 2))
    False
    >>> check_smaller((1, 2, 3), (4, 4, 1))
    False
    >>> check_smaller((1, 2, 3), (4, 3, 4))
    False
    >>> check_smaller((1, 2, 3), (4, 2, 4))
    False
    >>> check_smaller((1, 2, 3), (4, 1, 4))
    False
    >>> check_smaller((1, 2, 3), (4, 4, 3))
    False
    >>> check_smaller((1, 2, 3), (4, 4, 2))
    False
    >>> check_smaller((1, 2, 3), (4, 4, 1))
    False
    >>> check_smaller((1, 2, 3), (4, 3, 4))
    False