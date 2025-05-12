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
    >>> unique_sorted_by([(1, 2), (1, 3), (2, 4), (3, 5)], lambda x: x[0])
    [(1, 2), (2, 4), (3, 5)]
    """
    return sorted(list(set(l)), key=key)


def unique_sorted_by_reverse(l: list, key):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_reverse([(1, 2), (1, 3), (2, 4), (3, 5)], lambda x: x[0])
    [(3, 5), (2, 4), (1, 3), (1, 2)]
    """
    return sorted(list(set(l)), key=key, reverse=True)


def unique_sorted_by_reverse_by(l: list, key, reverse_key):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_reverse_by([(1, 2), (1, 3), (2, 4), (3, 5)], lambda x: x[0], lambda x: x[1])
    [(3, 5), (2, 4), (1, 3), (1, 2)]
    """
    return sorted(list(set(l)), key=key, reverse=True, reverse_key=reverse_key)


def unique_sorted_by_reverse_by_reverse(l: list, key, reverse_key):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_reverse_by_reverse([(1, 2), (1, 3), (2, 4), (3, 5)], lambda x: x[0], lambda x: x[1])
    [(1, 2), (1, 3), (2, 4), (3, 5)]
    """
    return sorted(list(set(l)), key=key, reverse=True, reverse_key=reverse_key, reverse_reverse_key=True)


def unique_sorted_by_reverse_by_reverse_by(l: list, key, reverse_key, reverse_reverse_key):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_reverse_by_reverse_by([(1, 2), (1, 3), (2, 4), (3, 5)], lambda x: x[0], lambda x: x[1], lambda x: x[0])
    [(1, 2), (1, 3), (2, 4), (3, 5)]
    """
    return sorted(list(set(l)), key=key, reverse=True, reverse_key=reverse_key, reverse_reverse_key=reverse_reverse_key)


def unique_sorted_by_reverse_by_reverse_by_reverse(l: list, key, reverse_key, reverse_reverse_key):
    """Return sorted unique elements in a list
    >>> unique_sorted_by_reverse_by_reverse_by_reverse([(1, 2), (1, 3), (2, 4), (3, 5)], lambda x: x[0], lambda x: x[1], lambda x: x[0])
    [(1, 2), (1, 3), (2, 4), (3, 5)]
    """
    return sorted(list