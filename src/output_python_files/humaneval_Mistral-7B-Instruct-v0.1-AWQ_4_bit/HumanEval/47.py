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
        return (l[n//2] + l[n//2 - 1]) / 2
    else:
        return l[n//2]


def median_of_two_sorted_arrays(a: list, b: list):
    """Return median of two sorted arrays a and b.
    >>> median_of_two_sorted_arrays([1, 2, 3], [4, 5, 6])
    3.0
    >>> median_of_two_sorted_arrays([-10, 4, 6, 1000, 10, 20], [10000, 100000, 1000000])
    100000.0
    """
    if len(a) == 0 or len(b) == 0:
        return 0
    if len(a) == 1 and len(b) == 1:
        return a[0] + b[0] / 2
    if len(a) == 1:
        return median(a + b)
    if len(b) == 1:
        return median(a + b)
    return median(a + b)


def median_of_three_sorted_arrays(a: list, b: list, c: list):
    """Return median of three sorted arrays a, b, and c.
    >>> median_of_three_sorted_arrays([1, 2, 3], [4, 5, 6], [7, 8, 9])
    5.0
    >>> median_of_three_sorted_arrays([-10, 4, 6, 1000, 10, 20], [10000, 100000, 1000000], [10000000, 100000000, 1000000000])
    100000000.0
    """
    if len(a) == 0 or len(b) == 0 or len(c) == 0:
        return 0
    if len(a) == 1 and len(b) == 1 and len(c) == 1:
        return a[0] + b[0] + c[0] / 3
    if len(a) == 1 and len(b) == 1:
        return median_of_two_sorted_arrays(a, b) + c[0] / 2
    if len(a) == 1:
        return median_of_two_sorted_arrays(a, b) + median_of_two_sorted_arrays(a, c) / 2
    if len(b) == 1:
        return median_of_two_sorted_arrays(a, b) + median_of_two_sorted_arrays(b, c) / 2
    if len(c) == 1:
        return median_of_two_sorted_arrays(a, b) + median_of_two_sorted_arrays(a, c) / 2
    return median_of_two_sorted_arrays(a, b) + median_of_two_sorted_arrays(b, c) / 2


def median