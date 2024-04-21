"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""


def find_solution(a, b, n):
    """
    >>> find_solution(2, 3, 7)
    (2, 1)
    >>> find_solution(2, 3, 10)
    (1, 3)
    >>> find_solution(2, 3, 11)
    """
    if a == 0:
        return None
    if a > 0:
        x = n // b
        y = n % b
        if x * a + y * b == n:
            return x, y
        else:
            return None
    else:
        x = n // b
        y = n % b
        if x * a + y * b == n:
            return x, y
        else:
            return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
</s>