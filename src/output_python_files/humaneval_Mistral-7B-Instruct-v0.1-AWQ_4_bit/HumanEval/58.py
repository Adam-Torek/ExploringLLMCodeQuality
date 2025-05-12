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


def common_with_order(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_with_order([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_with_order([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1 = sorted(list(set(l1)))
    l2 = sorted(list(set(l2)))
    return [x for x in l1 if x in l2]


def common_with_order_and_count(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_with_order_and_count([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_with_order_and_count([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1 = sorted(list(set(l1)))
    l2 = sorted(list(set(l2)))
    return [x for x in l1 if x in l2]


def common_with_order_and_count_and_reverse(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_with_order_and_count_and_reverse([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_with_order_and_count_and_reverse([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1 = sorted(list(set(l1)))
    l2 = sorted(list(set(l2)))
    return [x for x in l1 if x in l2]


def common_with_order_and_count_and_reverse_and_sort(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_with_order_and_count_and_reverse_and_sort([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_with_order_and_count_and_reverse_and_sort([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1 = sorted(list(set(l1)))
    l2 = sorted(list(set(l2)))
    return [x for x in l1 if x in l2]


def common_with_order_and_count_and_reverse_and_sort_and_reverse(l1: list, l2: list):
    """Return sorted unique common