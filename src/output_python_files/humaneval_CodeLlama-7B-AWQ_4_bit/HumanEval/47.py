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
    count = 1
    mode = l[0]
    for i in range(1, len(l)):
        if l[i] == l[i - 1]:
            count += 1
        else:
            if count > count:
                mode = l[i - 1]
            count = 1
    return mode


def variance(l: list):
    """Return variance of elements in the list l.
    >>> variance([3, 1, 2, 4, 5])
    2.0
    >>> variance([-10, 4, 6, 1000, 10, 20])
    10000000.0
    """
    mean_ = mean(l)
    variance = 0
    for i in l:
        variance += (i - mean_) ** 2
    return variance / len(l)


def standard_deviation(l: list):
    """Return standard deviation of elements in the list l.
    >>> standard_deviation([3, 1, 2, 4, 5])
    1.4142135623730951
    >>> standard_deviation([-10, 4, 6, 1000, 10, 20])
    1000.0
    """
    return variance(l) ** 0.5


def correlation(l1: list, l2: list):
    """Return correlation of elements in the list l1 and l2.
    >>> correlation([3, 1, 2, 4, 5], [1, 2, 3, 4, 5])
    1.0
    >>> correlation([3, 1, 2, 4, 5], [1, 2, 3, 4, 5, 6])
    0.9999999999999999
    >>> correlation([3, 1, 2, 4, 5], [1, 2, 3, 4, 5, 6])
    0.9999999999999999
    """
    l1_mean = mean(l1)
    l2_mean = mean(l2)
    l1_variance = variance(l1)
    l2_variance = variance(l2)
    l1_standard_deviation = standard_deviation(l