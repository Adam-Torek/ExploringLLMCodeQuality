def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]


def median_test(l):
    """Test median function."""
    assert median(l) == median_test(l)


if __name__ == '__main__':
    median_test([3, 1, 2, 4, 5])
    median_test([-10, 4, 6, 1000, 10, 20])