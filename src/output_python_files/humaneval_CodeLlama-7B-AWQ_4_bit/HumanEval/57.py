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
    if l[0] < l[1]:
        for i in range(1, len(l)):
            if l[i] < l[i - 1]:
                return False
    else:
        for i in range(1, len(l)):
            if l[i] > l[i - 1]:
                return False
    return True


def monotonic_decreasing(l: list):
    """Return True is list elements are monotonically decreasing.
    >>> monotonic_decreasing([1, 2, 4, 20])
    False
    >>> monotonic_decreasing([1, 20, 4, 10])
    True
    >>> monotonic_decreasing([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    if l[0] > l[1]:
        for i in range(1, len(l)):
            if l[i] > l[i - 1]:
                return False
    else:
        for i in range(1, len(l)):
            if l[i] < l[i - 1]:
                return False
    return True


def monotonic_increasing(l: list):
    """Return True is list elements are monotonically increasing.
    >>> monotonic_increasing([1, 2, 4, 20])
    True
    >>> monotonic_increasing([1, 20, 4, 10])
    False
    >>> monotonic_increasing([4, 1, 0, -10])
    False
    """
    if len(l) < 2:
        return True
    if l[0] < l[1]:
        for i in range(1, len(l)):
            if l[i] > l[i - 1]:
                return False
    else:
        for i in range(1, len(l)):
            if l[i] < l[i - 1]:
                return False
    return True


def is_sorted(l: list):
    """Return True is list elements are sorted.
    >>> is_sorted([1, 2, 4, 20])
    True
    >>> is_sorted([1, 20, 4, 10])
    False
    >>> is_sorted([4, 1, 0, -10])
    False
    """
    if len(l) < 2:
        return True
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            return False
    return True


def is_sorted_decreasing(l: list):
    """Return True is list elements are sorted decreasing.
    >>> is_sorted_decreasing([1, 2, 4, 20])
    False
    >>> is_sorted_decreasing([1, 20, 4, 10])
    True
    >>> is_sorted_decreasing([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            return False
    return True


def is_sorted_increasing(l: list):
    """Return True is list elements are sorted increasing.
    >>> is_sorted_increasing([1, 2, 4, 20])
    True
    >>> is_sorted_increasing([1, 20, 4,