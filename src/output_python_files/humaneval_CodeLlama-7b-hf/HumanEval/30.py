def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [x for x in l if x > 0]


def get_negative(l: list):
    """Return only negative numbers in the list.
    >>> get_negative([-1, 2, -4, 5, 6])
    [-1, -4, -10]
    >>> get_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-5, -3, -3, -10]
    """
    return [x for x in l if x < 0]


def get_zero(l: list):
    """Return only zero numbers in the list.
    >>> get_zero([-1, 2, -4, 5, 6])
    []
    >>> get_zero([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [0]
    """
    return [x for x in l if x == 0]


def get_even(l: list):
    """Return only even numbers in the list.
    >>> get_even([-1, 2, -4, 5, 6])
    []
    >>> get_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, 4, 0, 123]
    """
    return [x for x in l if x % 2 == 0]


def get_odd(l: list):
    """Return only odd numbers in the list.
    >>> get_odd([-1, 2, -4, 5, 6])
    [-1, 5, 6]
    >>> get_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [3, -5, -3, 1]
    """
    return [x for x in l if x % 2 != 0]


def get_first_negative(l: list):
    """Return the first negative number in the list.
    >>> get_first_negative([-1, 2, -4, 5, 6])
    -1
    >>> get_first_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -5
    """
    for x in l:
        if x < 0:
            return x


def get_last_negative(l: list):
    """Return the last negative number in the list.
    >>> get_last_negative([-1, 2, -4, 5, 6])
    -4
    >>> get_last_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    """
    for x in l[::-1]:
        if x < 0:
            return x


def get_first_positive(l: list):
    """Return the first positive number in the list.
    >>> get_first_positive([-1, 2, -4, 5, 6])
    2
    >>> get_first_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    5
    """
    for x in l:
        if x > 0: