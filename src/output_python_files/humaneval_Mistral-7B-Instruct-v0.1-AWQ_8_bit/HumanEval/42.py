def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]


def decr_list(l: list):
    """Return list with elements decremented by 1.
    >>> decr_list([1, 2, 3])
    [0, 1, 2]
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [4, 2, 4, 1, 2, 2, 8, 0, 122]
    """
    return [x - 1 for x in l]


def multiply_list(l: list):
    """Return list with elements multiplied by 2.
    >>> multiply_list([1, 2, 3])
    [2, 4, 6]
    >>> multiply_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [10, 6, 10, 4, 6, 6, 18, 0, 246]
    """
    return [x * 2 for x in l]


def reverse_list(l: list):
    """Return reversed list.
    >>> reverse_list([1, 2, 3])
    [3, 2, 1]
    >>> reverse_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [123, 9, 3, 3, 2, 5, 5, 0, 3]
    """
    return l[::-1]


def sum_list(l: list):
    """Return sum of list elements.
    >>> sum_list([1, 2, 3])
    6
    >>> sum_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    378
    """
    return sum(l)


def product_list(l: list):
    """Return product of list elements.
    >>> product_list([1, 2, 3])
    6
    >>> product_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    11107810000000000000
    """
    return 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20 * 21 * 22 * 23 * 24 * 25 * 26 * 27 * 28 * 29 * 30 * 31 * 32 * 33 * 34 * 35 * 36 * 37 * 38 * 39 * 40 * 41 * 42 * 43 * 44 * 45 * 46 * 47 * 48 * 49 * 50 * 51 * 52 * 53 * 54 * 55 * 56 * 57 * 58 * 59 * 60 * 61 * 62 * 63 * 64 * 65 * 66 * 67 * 68 * 69 * 70 * 71 * 72 * 73 * 74 * 75 * 76 *