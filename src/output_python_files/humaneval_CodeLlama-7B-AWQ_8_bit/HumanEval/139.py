def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    if n < 0:
        return None
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))


def test_special_factorial():
    assert special_factorial(4) == 288
    assert special_factorial(5) == 120
    assert special_factorial(6) == 720
    assert special_factorial(7) == 5040
    assert special_factorial(8) == 40320
    assert special_factorial(9) == 362880
    assert special_factorial(10) == 3628800
    assert special_factorial(11) == 39916800
    assert special_factorial(12) == 479001600
    assert special_factorial(13) == 6227020800
    assert special_factorial(14) == 87178291200
    assert special_factorial(15) == 1307674368000
    assert special_factorial(16) == 20922789888000
    assert special_factorial(17) == 355687428096000
    assert special_factorial(18) == 6