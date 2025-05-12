def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """

def get_negative(l: list):
    """Return only negative numbers in the list.
    >>> get_negative([-1, 2, -4, 5, 6])
    [-1, -4]
    >>> get_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-5, -3, -3, -10]
    """

def get_zero(l: list):
    """Return only zeroes in the list.
    >>> get_zero([-1, 2, -4, 5, 6])
    [0]
    >>> get_zero([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [0]
    """

def get_non_zero(l: list):
    """Return only non-zero numbers in the list.
    >>> get_non_zero([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_non_zero([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """

def get_unique(l: list):
    """Return only unique numbers in the list.
    >>> get_unique([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_unique([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """

def get_odd(l: list):
    """Return only odd numbers in the list.
    >>> get_odd([-1, 2, -4, 5, 6])
    [1, 3, 5, 7]
    >>> get_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [1, 3, 5, 7]
    """

def get_even(l: list):
    """Return only even numbers in the list.
    >>> get_even([-1, 2, -4, 5, 6])
    [2, 4, 6]
    >>> get_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, 4, 6]
    """

def get_positive_odd(l: list):
    """Return only positive odd numbers in the list.
    >>> get_positive_odd([-1, 2, -4, 5, 6])
    [1, 3, 5, 7]
    >>> get_positive_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [1, 3, 5, 7]
    """

def get_positive_even(l: list):
    """Return only positive even numbers in the list.
    >>> get_positive_even([-1, 2, -4, 5, 6])
    [2, 4, 6]
    >>> get_positive_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, 4, 6]
    """

def get_negative_odd(l: list):
    """Return only negative odd numbers in the list