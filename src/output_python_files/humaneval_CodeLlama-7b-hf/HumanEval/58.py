def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return sorted(set(l1) & set(l2))


def common_with_order(l1: list, l2: list):
    """Return sorted common elements for two lists.
    >>> common_with_order([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_with_order([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return sorted(list(set(l1) & set(l2)))


def common_with_order_2(l1: list, l2: list):
    """Return sorted common elements for two lists.
    >>> common_with_order_2([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_with_order_2([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return sorted(list(set(l1) & set(l2)))


def common_with_order_3(l1: list, l2: list):
    """Return sorted common elements for two lists.
    >>> common_with_order_3([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_with_order_3([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return sorted(list(set(l1) & set(l2)))


def common_with_order_4(l1: list, l2: list):
    """Return sorted common elements for two lists.
    >>> common_with_order_4([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_with_order_4([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return sorted(list(set(l1) & set(l2)))


def common_with_order_5(l1: list, l2: list):
    """Return sorted common elements for two lists.
    >>> common_with_order_5([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_with_order_5([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return sorted(list(set(l1) & set(l2)))


def common_with_order_6(l1: list, l2: list):
    """Return sorted common elements for two lists.
    >>> common_with_order_6([1, 4, 3, 34, 653, 2, 5], [5,