def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i > t:
            return False
    return True


def above_threshold(l: list, t: int):
    """Return True if all numbers in the list l are above threshold t.
    >>> above_threshold([1, 2, 4, 10], 1)
    False
    >>> above_threshold([1, 20, 4, 10], 5)
    True
    """
    for i in l:
        if i <= t:
            return False
    return True


def all_above_threshold(l: list, t: int):
    """Return True if all numbers in the list l are above threshold t.
    >>> all_above_threshold([1, 2, 4, 10], 1)
    False
    >>> all_above_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i <= t:
            return False
    return True


def all_below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> all_below_threshold([1, 2, 4, 10], 100)
    False
    >>> all_below_threshold([1, 20, 4, 10], 5)
    True
    """
    for i in l:
        if i > t:
            return False
    return True


def all_above_or_below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are above or below threshold t.
    >>> all_above_or_below_threshold([1, 2, 4, 10], 1)
    True
    >>> all_above_or_below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i <= t and i > t:
            return False
    return True


def all_above_or_below_threshold_2(l: list, t: int):
    """Return True if all numbers in the list l are above or below threshold t.
    >>> all_above_or_below_threshold_2([1, 2, 4, 10], 1)
    True
    >>> all_above_or_below_threshold_2([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i <= t or i > t:
            return False
    return True


def all_above_or_below_threshold_3(l: list, t: int):
    """Return True if all numbers in the list l are above or below threshold t.
    >>> all_above_or_below_threshold_3([1, 2, 4, 10], 1)
    True
    >>> all_above_or_below_threshold_3([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i <= t and i > t:
            return False
    return True


def all_above_or_below_threshold_4(l: list, t: int):
    """Return True if all numbers in the list l are above or below threshold t.
    >>> all_above_or_below