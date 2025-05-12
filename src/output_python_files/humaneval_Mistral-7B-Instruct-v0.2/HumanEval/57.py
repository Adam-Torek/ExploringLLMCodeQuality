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
    first = l[0]
    second = l[1]
    for i in range(1, len(l)):
        if first > second:
            return False
        first = second
        second = l[i+1]
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()