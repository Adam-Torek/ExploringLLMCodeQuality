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
    [-5, -3, -10]
    """

def get_even(l: list):
    """Return only even numbers in the list.
    >>> get_even([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> get_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, 4, 0, 123, -10]
    """

def get_odd(l: list):
    """Return only odd numbers in the list.
    >>> get_odd([1, 2, 3, 4, 5, 6])
    [1, 3, 5]
    >>> get_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, -5, 3, -3, 9, 1, -10]
    """

def get_divisible_by(l: list, n: int):
    """Return only numbers divisible by n in the list.
    >>> get_divisible_by([1, 2, 3, 4, 5, 6], 2)
    [2, 4, 6]
    >>> get_divisible_by([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 3)
    [3, -3, 3, 9, -10]
    """

def get_divisible_by_and_even(l: list):
    """Return only numbers divisible by 2 and even in the list.
    >>> get_divisible_by_and_even([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> get_divisible_by_and_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, 4, 0, 123, -10]
    """

def get_divisible_by_and_odd(l: list):
    """Return only numbers divisible by 2 and odd in the list.
    >>> get_divisible_by_and_odd([1, 2, 3, 4, 5, 6])
    [1, 3, 5]
    >>> get_divisible_by_and_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, -5, 3, -3, 9, 1, -10]
    """

def get_divisible_by_and_positive(l: list):
    """Return only numbers divisible by 2 and positive in the list.
    >>> get_divisible_by_and_positive([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> get_divisible_by_and_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, 4, 0, 123, -10]