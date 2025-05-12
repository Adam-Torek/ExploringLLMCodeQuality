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
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def monotonic_sort(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic_sort([1, 2, 4, 20])
    True
    >>> monotonic_sort([1, 20, 4, 10])
    False
    >>> monotonic_sort([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def monotonic_sort_with_duplicates(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic_sort_with_duplicates([1, 2, 4, 20])
    True
    >>> monotonic_sort_with_duplicates([1, 20, 4, 10])
    False
    >>> monotonic_sort_with_duplicates([4, 1, 0, -10, 1, 1, 1, 1])
    True
    """
    if len(l) < 2:
        return True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def monotonic_sort_with_duplicates_2(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic_sort_with_duplicates_2([1, 2, 4, 20])
    True
    >>> monotonic_sort_with_duplicates_2([1, 20, 4, 10])
    False
    >>> monotonic_sort_with_duplicates_2([4, 1, 0, -10, 1, 1, 1, 1])
    True
    """
    if len(l) < 2:
        return True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def monotonic_sort_with_duplicates_3(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic_sort_with_duplicates_3([1, 2, 4, 20])
    True
    >>> monotonic_sort_with_duplicates_3([1, 20, 4, 10])
    False
    >>> monotonic_sort_with_duplicates_3([4, 1, 0, -10, 1, 1, 1, 1])
    True
    """
    if len(l) < 2:
        return True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def monotonic_sort_with_duplicates_4(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic_sort_with_duplicates_4([1, 2, 4, 20])
    True
    >>> monotonic_