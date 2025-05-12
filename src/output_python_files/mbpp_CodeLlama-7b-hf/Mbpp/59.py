"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""


def is_octagonal(n):
    """
    >>> is_octagonal(5)
    True
    >>> is_octagonal(6)
    False
    """
    for i in range(1, n + 1):
        if is_octagonal_number(i):
            return True
    return False


def is_octagonal_number(n):
    """
    >>> is_octagonal_number(6)
    True
    >>> is_octagonal_number(7)
    False
    """
    for i in range(1, n + 1):
        if is_octagonal_number_helper(i, n):
            return True
    return False


def is_octagonal_number_helper(i, n):
    """
    >>> is_octagonal_number_helper(6, 5)
    True
    >>> is_octagonal_number_helper(7, 5)
    False
    """
    if i > n:
        return False
    if i * 3 + 1 == n:
        return True
    return is_octagonal_number_helper(i + 1, n)


if __name__ == "__main__":
    import doctest

    doctest.testmod()