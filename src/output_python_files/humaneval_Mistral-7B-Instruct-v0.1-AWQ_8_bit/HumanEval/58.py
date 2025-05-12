def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1 = sorted(list(set(l1)))
    l2 = sorted(list(set(l2)))
    return [x for x in l1 if x in l2]


def common_all(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_all([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_all([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1 = sorted(list(set(l1)))
    l2 = sorted(list(set(l2)))
    return [x for x in l1 if x in l2]


def common_all_2(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_all_2([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_all_2([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1 = sorted(list(set(l1)))
    l2 = sorted(list(set(l2)))
    return [x for x in l1 if x in l2]


def common_all_3(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_all_3([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_all_3([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1 = sorted(list(set(l1)))
    l2 = sorted(list(set(l2)))
    return [x for x in l1 if x in l2]


def common_all_4(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_all_4([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_all_4([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1 = sorted(list(set(l1)))
    l2 = sorted(list(set(l2)))
    return [x for x in l1 if x in l2]


def common_all_5(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_all_5([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_all_5([5, 3, 2, 8