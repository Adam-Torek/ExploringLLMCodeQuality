def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))


def unique_sorted(l: list):
    """Return sorted unique elements in a list
    >>> unique_sorted([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))


def unique_sorted_by(l: list, key):
    """Return sorted unique elements in a list
    >>> unique_sorted_by([(1, 2), (2, 3), (1, 4), (2, 5), (1, 6)], lambda x: x[0])
    [(1, 2), (2, 3), (1, 6)]
    """
    return sorted(list(set(l)), key=key)


def unique_sorted_by_key(l: list, key):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_key([(1, 2), (2, 3), (1, 4), (2, 5), (1, 6)], lambda x: x[0])
    [(1, 2), (2, 3), (1, 6)]
    """
    return sorted(list(set(l)), key=key)


def unique_sorted_by_key_value(l: list, key, value):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_key_value([(1, 2), (2, 3), (1, 4), (2, 5), (1, 6)], lambda x: x[0], lambda x: x[1])
    [(1, 2), (2, 3), (1, 6)]
    """
    return sorted(list(set(l)), key=key, value=value)


def unique_sorted_by_key_value_reverse(l: list, key, value):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_key_value_reverse([(1, 2), (2, 3), (1, 4), (2, 5), (1, 6)], lambda x: x[0], lambda x: x[1])
    [(1, 6), (2, 3), (1, 2)]
    """
    return sorted(list(set(l)), key=key, value=value, reverse=True)


def unique_sorted_by_key_value_reverse_key(l: list, key, value):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_key_value_reverse_key([(1, 2), (2, 3), (1, 4), (2, 5), (1, 6)], lambda x: x[0], lambda x: x[1])
    [(1, 6), (2, 3), (1, 2)]
    """
    return sorted(list(set(l