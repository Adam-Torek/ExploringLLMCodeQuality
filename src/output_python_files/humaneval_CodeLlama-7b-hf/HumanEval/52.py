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
    """
    return sum(l) / len(l)


def median(l: list):
    """Return the median of the numbers in the list l.
    >>> median([1, 2, 4, 10])
    4.0
    """
    l.sort()
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        return l[len(l) // 2]


def mode(l: list):
    """Return the mode of the numbers in the list l.
    >>> mode([1, 2, 4, 10])
    1
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
            else:
                if count < count:
                    mode = l[i]
    return mode


def variance(l: list):
    """Return the variance of the numbers in the list l.
    >>> variance([1, 2, 4, 10])
    10.0
    """
    avg = average(l)
    var = 0
    for i in l:
        var += (i - avg) ** 2
    return var / len(l)


def standard_deviation(l: list):
    """Return the standard deviation of the numbers in the list l.
    >>> standard_deviation([1, 2, 4, 10])
    3.1622776601683795
    """
    return variance(l) ** 0.5


def correlation(l1: list, l2: list):
    """Return the correlation of the lists l1 and l2.
    >>> correlation([1, 2, 4, 10], [1, 2, 4, 10])
    1.0
    """
    l1_avg = average(l1)
    l2_avg = average(l2)
    l1_var = variance(l1)
    l2_var = variance(l2)
    l1_l2_cov = 0
    for i in range(len(l1)):
        l1_l2_cov += (l1[i] - l1_avg) * (l2[i] - l2_avg)
    return l1_l2_cov / (len(l1) * l1_var * l2_var) ** 0.5


def covariance(l1: list, l2: list):
    """Return the covariance of the lists l1 and l2.
    >>> covariance([1, 2, 4, 10], [1, 2, 4, 10])
    0.0
    """
    l1_avg = average(l