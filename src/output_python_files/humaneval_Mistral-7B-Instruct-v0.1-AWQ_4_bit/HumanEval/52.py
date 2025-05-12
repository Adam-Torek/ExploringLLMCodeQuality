def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for x in l:
        if x >= t:
            return False
    return True


def above_threshold(l: list, t: int):
    """Return True if all numbers in the list l are above threshold t.
    >>> above_threshold([1, 2, 4, 10], 100)
    False
    >>> above_threshold([1, 20, 4, 10], 5)
    True
    """
    for x in l:
        if x <= t:
            return False
    return True


def threshold_range(l: list, t1: int, t2: int):
    """Return True if all numbers in the list l are between threshold t1 and t2.
    >>> threshold_range([1, 2, 4, 10], 1, 10)
    True
    >>> threshold_range([1, 20, 4, 10], 5, 10)
    False
    """
    for x in l:
        if x < t1 or x > t2:
            return False
    return True


def threshold_range_inclusive(l: list, t1: int, t2: int):
    """Return True if all numbers in the list l are between threshold t1 and t2,
    inclusive.
    >>> threshold_range_inclusive([1, 2, 4, 10], 1, 10)
    True
    >>> threshold_range_inclusive([1, 20, 4, 10], 5, 10)
    True
    """
    for x in l:
        if x < t1 or x > t2:
            return False
    return True


def threshold_range_exclusive(l: list, t1: int, t2: int):
    """Return True if all numbers in the list l are between threshold t1 and t2,
    exclusive.
    >>> threshold_range_exclusive([1, 2, 4, 10], 1, 10)
    True
    >>> threshold_range_exclusive([1, 20, 4, 10], 5, 10)
    False
    """
    for x in l:
        if x < t1 or x > t2:
            return False
    return True


def threshold_range_exclusive_inclusive(l: list, t1: int, t2: int):
    """Return True if all numbers in the list l are between threshold t1 and t2,
    exclusive.
    >>> threshold_range_exclusive_inclusive([1, 2, 4, 10], 1, 10)
    True
    >>> threshold_range_exclusive_inclusive([1, 20, 4, 10], 5, 10)
    False
    """
    for x in l:
        if x < t1 or x > t2:
            return False
    return True


def threshold_range_exclusive_inclusive_exclusive(l: list, t1: int, t2: int):
    """Return True if all numbers in the list l are between threshold t1 and t2,
    exclusive.
    >>> threshold_range_exclusive_inclusive_exclusive([1, 2, 4, 10], 1, 10)
    True
    >>> threshold_range_exclusive_inclusive_exclusive([1, 20, 4, 10], 5, 10)
    False
    """