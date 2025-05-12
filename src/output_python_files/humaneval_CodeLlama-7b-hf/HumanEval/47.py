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


def median_of_medians(l: list):
    """Return median of medians of the list l.
    >>> median_of_medians([3, 1, 2, 4, 5])
    3
    >>> median_of_medians([-10, 4, 6, 1000, 10, 20])
    10
    """
    if len(l) == 1:
        return l[0]
    elif len(l) % 2 == 0:
        return median([median(l[i:i + 2]) for i in range(0, len(l), 2)])
    else:
        return median(l)


def median_of_medians_recursive(l: list):
    """Return median of medians of the list l.
    >>> median_of_medians_recursive([3, 1, 2, 4, 5])
    3
    >>> median_of_medians_recursive([-10, 4, 6, 1000, 10, 20])
    10
    """
    if len(l) == 1:
        return l[0]
    elif len(l) % 2 == 0:
        return median([median_of_medians_recursive(l[i:i + 2]) for i in range(0, len(l), 2)])
    else:
        return median_of_medians_recursive(l)


def median_of_medians_recursive_2(l: list):
    """Return median of medians of the list l.
    >>> median_of_medians_recursive_2([3, 1, 2, 4, 5])
    3
    >>> median_of_medians_recursive_2([-10, 4, 6, 1000, 10, 20])
    10
    """
    if len(l) == 1:
        return l[0]
    elif len(l) % 2 == 0:
        return median([median_of_medians_recursive_2(l[i:i + 2]) for i in range(0, len(l), 2)])
    else:
        return median_of_medians_recursive_2(l)


def median_of_medians_recursive_3(l: list):
    """Return median of medians of the list l.
    >>> median_of_medians_recursive_3([3, 1, 2, 4, 5])
    3
    >>> median_of_medians_recursive_3([-10, 4, 6, 1000, 10, 20])
    10
    """
    if len(l) == 1:
        return l[0]
    elif len(l) % 2 == 0:
        return median([median_of_medians_recursive_3(l[i:i + 2]) for i in range(0, len(l), 2)])
    else:
        return median_of_medians_