def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:
        return 0
    elif len(xs) == 2:
        return xs[1]
    else:
        return xs[1] + xs[2] * x + sum(derivative(xs[3:]) * xs[2:])

def integral(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integral([3, 1, 2, 4, 5])
    [15/2]
    >>> integral([1, 2, 3])
    [1/2]
    """
    if len(xs) == 1:
        return 0
    elif len(xs) == 2:
        return xs[1] * xs[0] / 2
    else:
        return (xs[1] * xs[0] / 2) + sum(integral(xs[3:]) * xs[2:])

def test_integral():
    """
    >>> integral([1, 2, 3])
    1.5
    >>> integral([1, 2, 3, 4, 5])
    10.5
    >>> integral([3, 1, 2, 4, 5])
    15.0
    >>> integral([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    120.0
    >>> integral([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    364.5
    >>> integral([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,