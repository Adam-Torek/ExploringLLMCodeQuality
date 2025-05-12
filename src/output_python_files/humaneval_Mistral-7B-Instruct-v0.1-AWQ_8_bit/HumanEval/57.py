def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            return False
    return True


def monotonic_increasing(l: list):
    """Return True if list elements are monotonically increasing.
    >>> monotonic_increasing([1, 2, 4, 20])
    True
    >>> monotonic_increasing([1, 20, 4, 10])
    False
    >>> monotonic_increasing([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            return False
    return True


def monotonic_decreasing(l: list):
    """Return True if list elements are monotonically decreasing.
    >>> monotonic_decreasing([1, 2, 4, 20])
    False
    >>> monotonic_decreasing([1, 20, 4, 10])
    True
    >>> monotonic_decreasing([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            return False
    return True


def monotonic_sorted(l: list):
    """Return True if list elements are monotonically sorted.
    >>> monotonic_sorted([1, 2, 4, 20])
    True
    >>> monotonic_sorted([1, 20, 4, 10])
    False
    >>> monotonic_sorted([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            return False
    return True


def monotonic_sorted_increasing(l: list):
    """Return True if list elements are monotonically sorted in increasing order.
    >>> monotonic_sorted_increasing([1, 2, 4, 20])
    True
    >>> monotonic_sorted_increasing([1, 20, 4, 10])
    False
    >>> monotonic_sorted_increasing([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            return False
    return True


def monotonic_sorted_decreasing(l: list):
    """Return True if list elements are monotonically sorted in decreasing order.
    >>> monotonic_sorted_decreasing([1, 2, 4, 20])
    False
    >>> monotonic_sorted_decreasing([1, 20, 4, 10])
    True
    >>> monotonic_sorted_decreasing([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            return False
    return True


def monotonic_sorted_increasing_decreasing(l: list):
    """Return True if list elements are monotonically sorted