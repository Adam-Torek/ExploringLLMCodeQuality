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
    return list(filter(lambda x: x > 0, map(lambda x: x + 1, l)))


def incr_list_reduce(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_reduce([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_reduce([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return list(reduce(lambda x, y: x + [y + 1], l, []))


def incr_list_reduce_lambda(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_reduce_lambda([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_reduce_lambda([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return list(reduce(lambda x, y: x + [y + 1], l, []))


def incr_list_reduce_lambda_comp(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_reduce_lambda_comp([1, 2, 3])