def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]


def mean(l: list):
    """Return mean of elements in the list l.
    >>> mean([3, 1, 2, 4, 5])
    3.0
    >>> mean([-10, 4, 6, 1000, 10, 20])
    10.0
    """
    return sum(l) / len(l)


def mode(l: list):
    """Return mode of elements in the list l.
    >>> mode([3, 1, 2, 4, 5])
    1
    >>> mode([-10, 4, 6, 1000, 10, 20])
    10
    """
    l.sort()
    count = 0
    mode = l[0]
    for i in range(len(l)):
        if l[i] == l[i + 1]:
            count += 1
        else:
            if count > 1:
                return mode
            mode = l[i + 1]
            count = 1
    return mode


def variance(l: list):
    """Return variance of elements in the list l.
    >>> variance([3, 1, 2, 4, 5])
    2.0
    >>> variance([-10, 4, 6, 1000, 10, 20])
    100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000