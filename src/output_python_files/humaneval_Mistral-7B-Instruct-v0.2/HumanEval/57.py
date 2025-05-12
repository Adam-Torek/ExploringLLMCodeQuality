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
    elif l[0] < l[1]:
        return all(x < y for x, y in zip(l, l[1:]))
    else:
        return all(x > y for x, y in zip(l, l[1:]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()