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


def all_below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> all_below_threshold([1, 2, 4, 10], 100)
    True
    >>> all_below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i >= t:
            return False
    return True


def all_above_threshold(l: list, t: int):
    """Return True if all numbers in the list l are above threshold t.
    >>> all_above_threshold([1, 2, 4, 10], 1)
    False
    >>> all_above_threshold([1, 20, 4, 10], 5)
    True
    """
    for i in l:
        if i <= t:
            return False
    return True


def all_equal(l: list):
    """Return True if all numbers in the list l are equal.
    >>> all_equal([1, 2, 4, 10])
    False
    >>> all_equal([1, 2, 4, 10, 10])
    True
    """
    for i in range(len(l) - 1):
        if l[i] != l[i + 1]:
            return False
    return True


def all_equal_except_one(l: list):
    """Return True if all numbers in the list l are equal except one.
    >>> all_equal_except_one([1, 2, 4, 10])
    True
    >>> all_equal_except_one([1, 2, 4, 10, 10])
    False
    """
    for i in range(len(l) - 1):
        if l[i] != l[i + 1]:
            return False
    return True


def all_equal_except_two(l: list):
    """Return True if all numbers in the list l are equal except two.
    >>> all_equal_except_two([1, 2, 4, 10])
    True
    >>> all_equal_except_two([1, 2, 4, 10, 10])
    False
    """
    for i in range(len(l) - 2):
        if l[i] != l[i + 2]:
            return False
    return True


def all_equal_except_three(l: list):
    """Return True if all numbers in the list l are equal except three.
    >>> all_equal_except_three([1, 2, 4, 10])
    True
    >>> all_equal_except_three([1, 2, 4, 10, 10])
    False
    """
    for i in range