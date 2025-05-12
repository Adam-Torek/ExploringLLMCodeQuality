def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return sorted(list(set(l1) & set(l2)))


def common_with_count(l1: list, l2: list):
    """Return sorted unique common elements with count for two lists.
    >>> common_with_count([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [(1, 2), (5, 2), (653, 2)]
    >>> common_with_count([5, 3, 2, 8], [3, 2])
    [(2, 2), (3, 2)]

    """
    return sorted(list(set(l1) & set(l2)), key=lambda x: (x[1], x[0]))


def common_with_count_dict(l1: list, l2: list):
    """Return sorted unique common elements with count for two lists.
    >>> common_with_count_dict([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    {1: 2, 5: 2, 653: 2}
    >>> common_with_count_dict([5, 3, 2, 8], [3, 2])
    {2: 2, 3: 2}

    """
    return dict(common_with_count(l1, l2))


def common_with_count_dict_sorted(l1: list, l2: list):
    """Return sorted unique common elements with count for two lists.
    >>> common_with_count_dict_sorted([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [(1, 2), (5, 2), (653, 2)]
    >>> common_with_count_dict_sorted([5, 3, 2, 8], [3, 2])
    [(2, 2), (3, 2)]

    """
    return sorted(common_with_count_dict(l1, l2).items(), key=lambda x: (x[1], x[0]))


def common_with_count_dict_sorted_by_value(l1: list, l2: list):
    """Return sorted unique common elements with count for two lists.
    >>> common_with_count_dict_sorted_by_value([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [(2, 2), (3, 2), (1, 2), (5, 2), (653, 2)]
    >>> common_with_count_dict_sorted_by_value([5, 3, 2, 8], [3, 2])
    [(2, 2), (3, 2)]

    """
    return sorted(common_with_count_dict(l1, l2).items(), key=lambda x: (x[1], x[0]))


def common_with_count_dict_sorted_by_value_reverse(l1: list, l2: list):
    """Return sorted unique common elements with count for two lists.
    >>> common_with_count_dict_sorted_by_value_reverse([1, 4, 3, 34,