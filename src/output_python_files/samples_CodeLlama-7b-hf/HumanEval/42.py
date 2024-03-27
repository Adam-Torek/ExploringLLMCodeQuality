def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]


def incr_list_comp(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_comp([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_comp([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]


def incr_list_map(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_map([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_map([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return list(map(lambda x: x + 1, l))


def incr_list_filter(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_filter([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_filter([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return list(filter(lambda x: x % 2 == 0, l))


def incr_list_reduce(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_reduce([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_reduce([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return list(reduce(lambda x, y: x + y, l))


def incr_list_zip(l1: list, l2: list):
    """Return list with elements incremented by 1.
    >>> incr_list_zip([1, 2, 3], [4, 5, 6])
    [5, 7, 9]
    >>> incr_list_zip([5, 3, 5, 2, 3, 3, 9, 0, 123], [1, 2, 3, 4, 5, 6, 7, 8, 9])
    [6, 5, 6, 5, 6, 6, 16, 9, 124]
    """
    return list(zip(l1, l2))


def incr_list_zip_map(l1: list, l2: list):
    """Return list with elements incremented by 1.
    >>> incr_list_zip_map([1, 2, 3], [4, 5, 6])
    [5, 7, 9]
    >>> incr_list_zip_map([5, 3, 5, 2, 3, 3, 9, 0, 1