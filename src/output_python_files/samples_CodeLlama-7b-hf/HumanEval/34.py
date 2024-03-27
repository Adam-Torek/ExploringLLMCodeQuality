def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))


def unique_sorted(l: list):
    """Return sorted unique elements in a list
    >>> unique_sorted([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))


def unique_sorted_by(l: list, key):
    """Return sorted unique elements in a list
    >>> unique_sorted_by([(5, 1), (3, 2), (5, 3), (2, 4), (3, 5), (3, 6), (9, 7), (0, 8), (123, 9)], lambda x: x[0])
    [(0, 8), (2, 4), (3, 6), (5, 1), (9, 7), (123, 9)]
    """
    return sorted(set(l), key=key)


def unique_sorted_by_key(l: list, key):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_key([(5, 1), (3, 2), (5, 3), (2, 4), (3, 5), (3, 6), (9, 7), (0, 8), (123, 9)], lambda x: x[0])
    [(0, 8), (2, 4), (3, 6), (5, 1), (9, 7), (123, 9)]
    """
    return sorted(set(l), key=key)


def unique_sorted_by_key_value(l: list, key):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_key_value([(5, 1), (3, 2), (5, 3), (2, 4), (3, 5), (3, 6), (9, 7), (0, 8), (123, 9)], lambda x: x[0])
    [(0, 8), (2, 4), (3, 6), (5, 1), (9, 7), (123, 9)]
    """
    return sorted(set(l), key=key)


def unique_sorted_by_key_value_tuple(l: list, key):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_key_value_tuple([(5, 1), (3, 2), (5, 3), (2, 4), (3, 5), (3, 6), (9, 7), (0, 8), (123, 9)], lambda x: x[0])
    [(0, 8), (2, 4), (3, 6), (5, 1), (9, 7), (123, 9)]
    """
    return sorted(set(l), key=key)


def unique_sorted_by_key_value_dict(l: list, key):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_key_value_dict([(5, 1), (3, 2), (5, 3), (2, 4), (3, 5), (3, 6), (9, 7), (0, 8), (123, 9)], lambda x: x[0])
    [(0, 8), (2, 4), (3, 6), (5, 1), (9, 7), (123, 9)]
    """
    return sorted(set(l), key=key)


def unique_sorted_by_key_value_dict_tuple(l: list, key):
    """Return sorted unique elements in a list