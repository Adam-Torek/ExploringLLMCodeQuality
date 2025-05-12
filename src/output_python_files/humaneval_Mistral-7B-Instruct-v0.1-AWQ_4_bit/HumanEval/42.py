def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]


def decr_list(l: list):
    """Return list with elements decremented by 1.
    >>> decr_list([1, 2, 3])
    [0, 1, 2]
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [4, 2, 4, 1, 2, 2, 8, 0, 122]
    """
    return [i - 1 for i in l]


def multiply_list(l: list):
    """Return list with elements multiplied by 2.
    >>> multiply_list([1, 2, 3])
    [2, 4, 6]
    >>> multiply_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [10, 6, 10, 4, 6, 6, 18, 0, 246]
    """
    return [i * 2 for i in l]


def divide_list(l: list):
    """Return list with elements divided by 2.
    >>> divide_list([1, 2, 3])
    [0.5, 1, 1.5]
    >>> divide_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2.5, 1.5, 2.5, 1, 1.5, 1.5, 4.5, 0, 61.5]
    """
    return [i / 2 for i in l]


def add_list(l: list):
    """Return list with elements added together.
    >>> add_list([1, 2, 3])
    6
    >>> add_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    372
    """
    return sum(l)


def sub_list(l: list):
    """Return list with elements subtracted together.
    >>> sub_list([1, 2, 3])
    -1
    >>> sub_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    -371
    """
    return -sum(l)


def max_list(l: list):
    """Return max element in list.
    >>> max_list([1, 2, 3])
    3
    >>> max_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    123
    """
    return max(l)


def min_list(l: list):
    """Return min element in list.
    >>> min_list([1, 2, 3])
    1
    >>> min_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    0
    """
    return min(l)


def avg_list(l: list):
    """Return average of list.
    >>> avg_list