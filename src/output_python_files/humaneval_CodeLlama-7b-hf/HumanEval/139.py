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
        return 0
    else:
        return n * special_factorial(n-1)


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
    assert special_factorial(18) == 6402373705728000
    assert special_factorial(19) == 121645100408832000
    assert special_factorial(20) == 2432902008176640000
    assert special_factorial(21) == 51090942171709440000
    assert special_factorial(22) == 1124000727777607680000
    assert special_factorial(23) == 25852016738884976640000
    assert special_factorial(24) == 6204484017332394393600000
    assert special_factorial(25) == 155112100433309859840000000
    assert special_factorial(26) == 40329146112660563558400000000
    assert special_factorial(27) == 10886456605651637682272000000000
    assert special_factorial(28) == 3048883446117138605015625000000000
    assert special_factorial(29) == 88417619937397019545436160000000000
    assert special_factorial(30) == 2652528598121910586363084800000000000
    assert special_factorial(31) == 81038305753059273135593750000000000000
    assert special_factorial(32) == 265252859812191