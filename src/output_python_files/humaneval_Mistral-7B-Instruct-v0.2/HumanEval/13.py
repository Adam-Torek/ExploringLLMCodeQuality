def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()