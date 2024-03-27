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


def average(l: list):
    """Return the average of the numbers in the list l.
    >>> average([1, 2, 4, 10])
    4.0
    >>> average([1, 2, 4, 10, 100])
    33.25
    """
    return sum(l) / len(l)


def median(l: list):
    """Return the median of the numbers in the list l.
    >>> median([1, 2, 4, 10])
    4.0
    >>> median([1, 2, 4, 10, 100])
    6.0
    """
    l.sort()
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        return l[len(l) // 2]


def mode(l: list):
    """Return the mode of the numbers in the list l.
    >>> mode([1, 2, 4, 10])
    10
    >>> mode([1, 2, 4, 10, 100])
    2
    """
    l.sort()
    count = 1
    mode = l[0]
    for i in range(1, len(l)):
        if l[i] == l[i - 1]:
            count += 1
        else:
            if count > 1:
                count = 1
                mode = l[i]
    return mode


def variance(l: list):
    """Return the variance of the numbers in the list l.
    >>> variance([1, 2, 4, 10])
    100.0
    >>> variance([1, 2, 4, 10, 100])
    10000.0
    """
    avg = average(l)
    var = 0
    for i in l:
        var += (i - avg) ** 2
    return var / len(l)


def standard_deviation(l: list):
    """Return the standard deviation of the numbers in the list l.
    >>> standard_deviation([1, 2, 4, 10])
    10.0
    >>> standard_deviation([1, 2, 4, 10, 100])
    100.0
    """
    return variance(l) ** 0.5


def correlation(l1: list, l2: list):
    """Return the correlation coefficient of the lists l1 and l2.
    >>> correlation([1, 2, 4, 10], [1, 2, 4, 10])
    1.0
    >>> correlation([1, 2, 4, 10], [1, 2, 4, 100])
    0.0
    """
    avg1 = average(l1)
    avg2 = average(l2)
    var1 = variance(l1)
    var2 = variance(l2)
    cov = 0
    for i in range(len(l1)):
        cov += (l1[i] - avg