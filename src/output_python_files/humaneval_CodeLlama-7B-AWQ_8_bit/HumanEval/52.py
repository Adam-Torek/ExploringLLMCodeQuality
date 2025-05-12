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


def all_below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> all_below_threshold([1, 2, 4, 10], 100)
    True
    >>> all_below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i > t:
            return False
    return True


def all_above_threshold(l: list, t: int):
    """Return True if all numbers in the list l are above threshold t.
    >>> all_above_threshold([1, 2, 4, 10], 100)
    False
    >>> all_above_threshold([1, 20, 4, 10], 5)
    True
    """
    for i in l:
        if i <= t:
            return False
    return True


def all_above_threshold_2(l: list, t: int):
    """Return True if all numbers in the list l are above threshold t.
    >>> all_above_threshold_2([1, 2, 4, 10], 100)
    False
    >>> all_above_threshold_2([1, 20, 4, 10], 5)
    True
    """
    return all(i > t for i in l)


def all_below_threshold_2(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> all_below_threshold_2([1, 2, 4, 10], 100)
    True
    >>> all_below_threshold_2([1, 20, 4, 10], 5)
    False
    """
    return all(i <= t for i in l)


def all_between_threshold(l: list, t1: int, t2: int):
    """Return True if all numbers in the list l are between threshold t1 and t2.
    >>> all_between_threshold([1, 2, 4, 10], 1, 10)
    True
    >>> all_between_threshold([1, 2, 4, 10], 1, 5)
    False
    """
    for i in l:
        if i < t1 or i > t2:
            return False
    return True


def all_between_threshold_2(l: list, t1: int, t2: int):
    """Return True if all numbers in the list l are between threshold t1 and t2.
    >>> all_between_threshold_2([1, 2, 4, 10], 1, 10)
    True
    >>> all_between_threshold_2([1, 2, 4, 10], 1, 5)
    False
    """
    return all(t1 <= i <= t2 for i in l)


def all_between_threshold_3(l: list, t1: int, t2: int):
    """Return True if all numbers in the list l are between threshold t1 and t2.
    >>> all_between_threshold_3([1, 2, 4, 10], 1, 10)
    True
    >>> all_between_threshold_3([1, 2, 4, 10], 1, 5)
    False
    """
    return all(t1 <= i < t2 for i in l)


def all_between_threshold_4(l: list, t1: int, t2: