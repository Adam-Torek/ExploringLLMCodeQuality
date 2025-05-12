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
    [-1, -4]
    >>> get_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-1, -5, -3, -10]
    """
    return [x for x in l if x < 0]


def get_zeros(l: list):
    """Return only zeros in the list.
    >>> get_zeros([-1, 2, -4, 5, 6])
    []
    >>> get_zeros([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [0]
    """
    return [x for x in l if x == 0]

def get_odd(l: list):
    """Return only odd numbers in the list.
    >>> get_odd([-1, 2, -4, 5, 6])
    [-1, 5, 3]
    >>> get_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 3, 1]
    """
    return [x for x in l if x % 2 != 0]

def get_even(l: list):
    """Return only even numbers in the list.
    >>> get_even([-1, 2, -4, 5, 6])
    [2, 6]
    >>> get_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, 6]
    """
    return [x for x in l if x % 2 == 0]

def get_divisible_by_3(l: list):
    """Return only numbers divisible by 3 in the list.
    >>> get_divisible_by_3([-1, 2, -4, 5, 6])
    [5]
    >>> get_divisible_by_3([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 123]
    """
    return [x for x in l if x % 3 == 0]

def get_divisible_by_4(l: list):
    """Return only numbers divisible by 4 in the list.
    >>> get_divisible_by_4([-1, 2, -4, 5, 6])
    [-4]
    >>> get_divisible_by_4([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-4]
    """
    return [x for x in l if x % 4 == 0]

def get_divisible_by_5(l: list):
    """Return only numbers divisible by 5 in the list.
    >>> get_divisible_by_5([-1, 2, -4, 5, 6])
    [5]
    >>> get_divisible_by_5([5, 3, -5, 2, -3, 3, 9,