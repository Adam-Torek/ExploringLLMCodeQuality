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

def get_odd_numbers(l: list):
    """Return only odd numbers in the list.
    >>> get_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [1, 3, 5, 7, 9]
    >>> get_odd_numbers([2, 4, 6, 8, 10, 12])
    []
    """
    return [x for x in l if x % 2 != 0]

def get_even_numbers(l: list):
    """Return only even numbers in the list.
    >>> get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [2, 4, 6, 8]
    >>> get_even_numbers([1, 3, 5, 7, 9])
    []
    """
    return [x for x in l if x % 2 == 0]

def get_divisible_by_3(l: list):
    """Return only numbers divisible by 3 in the list.
    >>> get_divisible_by_3([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [3, 6]
    >>> get_divisible_by_3([1, 4, 7, 10, 9])
    [3, 9]
    """
    return [x for x in l if x % 3 == 0]

def get_divisible_by_4(l: list):
    """Return only numbers divisible by 4 in the list.
    >>> get_divisible_by_4([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [4]
    >>> get_divisible_by_4([1, 4, 7, 10, 9])
    [4]
    """
    return [x for x in l if x % 4 == 0]

def get_divisible_by_5(l: list):
    """Return only numbers divisible by 5 in the list.
    >>> get_divisible_by_5([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [5]
    >>> get_divisible_by_5([1, 4, 7, 10, 9])
    [5]
    """
    return [x for x in l if