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
    >>> is_octagonal_number(65)
    True
    >>> is_octagonal_number(66)
    False
    """
    for i in range(1, n + 1):
        if is_octagonal_number_helper(i, n):
            return True
    return False


def is_octagonal_number_helper(n, target):
    """
    >>> is_octagonal_number_helper(65, 65)
    True
    >>> is_octagonal_number_helper(65, 66)
    False
    """
    if n == target:
        return True
    if n > target:
        return False
    return is_octagonal_number_helper(n + 1, target)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
