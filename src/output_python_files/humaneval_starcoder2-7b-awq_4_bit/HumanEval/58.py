def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

def common_with_counts(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_with_counts([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [(1, 1), (5, 2), (653, 2)]
    >>> common_with_counts([5, 3, 2, 8], [3, 2])
    [(2, 1), (3, 2)]

    """

def common_with_counts_and_positions(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_with_counts_and_positions([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [(1, 1, 0), (5, 2, 1), (653, 2, 4)]
    >>> common_with_counts_and_positions([5, 3, 2, 8], [3, 2])
    [(2, 1, 1), (3, 2, 0)]

    """

def common_with_counts_and_positions_and_indices(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_with_counts_and_positions_and_indices([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [(1, 1, 0, 0), (5, 2, 1, 1), (653, 2, 4, 4)]
    >>> common_with_counts_and_positions_and_indices([5, 3, 2, 8], [3, 2])
    [(2, 1, 1, 1), (3, 2, 0, 0)]

    """

def common_with_counts_and_positions_and_indices_and_values(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_with_counts_and_positions_and_indices_and_values([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [(1, 1, 0, 0, 1), (5, 2, 1, 1, 5), (653, 2, 4, 4, 653)]
    >>> common_with_counts_and_positions_and_indices_and_values([5, 3, 2, 8], [3, 2])
    [(2, 1, 1, 1, 2), (3, 2, 0, 0, 3)]

    """

def common_with_counts_and_positions_and_indices_and_values_and_indices(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_with_counts_and_positions_and_indices_and_values_and_indices([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [(1, 1, 0, 0, 1, 0), (5, 2, 1, 1, 5,