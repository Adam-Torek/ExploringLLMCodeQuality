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
    >>> get_even([-1, 2, 4, 5, 6])
    [2, 4, 6]
    >>> get_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, 4, 6, 123]
    """
    return [x for x in l if x % 2 == 0]


def get_odd(l: list):
    """Return only odd numbers in the list.
    >>> get_odd([-1, 2, 4, 5, 6])
    [1, 5, 6]
    >>> get_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [1, 3, 9, 123]
    """
    return [x for x in l if x % 2 != 0]


def get_sum(l: list):
    """Return the sum of all numbers in the list.
    >>> get_sum([1, 2, 3, 4, 5])
    15
    >>> get_sum([-1, 2, 3, 4, 5])
    15
    >>> get_sum([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    168
    """
    return sum(l)


def get_max(l: list):
    """Return the maximum number in the list.
    >>> get_max([1, 2, 3, 4, 5])
    5
    >>> get_max([-1, 2, 3, 4, 5])
    5
    >>> get_max([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)


def get_min(l: list):
    """Return the minimum number in the list.
    >>> get_min([1, 2, 3, 4, 5])
    1
    >>> get_min([-1, 2, 3, 4, 5])
    -1
    >>> get_min([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    """
    return min(l)


def get_avg(l: list):
    """Return the average of all numbers in the list.
    >>> get_avg([1, 2, 3, 4, 5])
    3.0
    >>> get_avg([-1, 2, 3, 4, 5])
    3.0
    >>> get_avg([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    10.0
    """
    return sum(l) / len(l)


def get_count(l: list):
    """Return the number of elements in the list.
    >>> get_count([1, 2, 3, 4, 5])
    5
    >>> get_count([-1, 2, 3, 4, 5])
    5
    >>>