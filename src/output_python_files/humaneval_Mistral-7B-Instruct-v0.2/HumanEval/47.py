def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    n = len(l)
    mid = n // 2
    if n % 2 == 0:
        return (l[mid - 1] + l[mid]) / 2
    else:
        return l[mid]


if __name__ == "__main__":
    import doctest
    doctest.testmod()</s>