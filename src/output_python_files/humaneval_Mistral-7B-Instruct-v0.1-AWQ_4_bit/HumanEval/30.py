def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [x for x in l if x > 0]


def get_even(l: list):
    """Return only even numbers in the list.
    >>> get_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [2, 4, 6, 8, 10]
    >>> get_even([-2, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [2, 4, 6, 8, 10]
    """
    return [x for x in l if x % 2 == 0]


def get_odd(l: list):
    """Return only odd numbers in the list.
    >>> get_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 3, 5, 7, 9]
    >>> get_odd([-2, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 3, 5, 7, 9]
    """
    return [x for x in l if x % 2 != 0]


def get_even_and_odd(l: list):
    """Return even and odd numbers in the list.
    >>> get_even_and_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
    >>> get_even_and_odd([-2, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
    """
    even, odd = get_even(l), get_odd(l)
    return even, odd


def get_even_and_positive(l: list):
    """Return even and positive numbers in the list.
    >>> get_even_and_positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
    >>> get_even_and_positive([-2, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
    """
    even, positive = get_even(l), get_positive(l)
    return even, positive


def get_even_and_negative(l: list):
    """Return even and negative numbers in the list.
    >>> get_even_and_negative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ([], [2, 4, 6, 8, 10])
    >>> get_even_and_negative([-2, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ([], [2, 4, 6, 8, 10])
    """