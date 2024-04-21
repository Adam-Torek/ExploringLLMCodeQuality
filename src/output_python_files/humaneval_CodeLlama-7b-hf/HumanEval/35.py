def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    """
    return min(l)


def sum_elements(l: list):
    """Return sum of all elements in the list.
    >>> sum_elements([1, 2, 3])
    6
    >>> sum_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return sum(l)


def average_elements(l: list):
    """Return average of all elements in the list.
    >>> average_elements([1, 2, 3])
    2.0
    >>> average_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    10.0
    """
    return sum_elements(l) / len(l)


def median_elements(l: list):
    """Return median of all elements in the list.
    >>> median_elements([1, 2, 3])
    2.0
    >>> median_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    3.0
    """
    l.sort()
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        return l[len(l) // 2]


def mode_elements(l: list):
    """Return mode of all elements in the list.
    >>> mode_elements([1, 2, 3])
    1
    >>> mode_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    3
    """
    l.sort()
    count = 0
    mode = l[0]
    for i in range(len(l)):
        if l[i] == mode:
            count += 1
        else:
            if count > 0:
                count = 0
                mode = l[i]
    return mode


def variance_elements(l: list):
    """Return variance of all elements in the list.
    >>> variance_elements([1, 2, 3])
    0.6666666666666666
    >>> variance_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    104.66666666666666
    """
    avg = average_elements(l)
    var = 0
    for i in range(len(l)):
        var += (l[i] - avg) ** 2
    return var / len(l)


def standard_deviation_elements(l: list):
    """Return standard deviation of all elements in the list.
    >>> standard_deviation_elements([1, 2, 3])
    0.816496580927726
    >>> standard_deviation_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    10.