def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [x * (len(xs) - i) for i, x in enumerate(xs[1:])]


def integral(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integral([3, 1, 2, 4, 5])
    [3, 1, 2, 4, 5]
    >>> integral([1, 2, 3])
    [1, 2, 3]
    """
    return [x / (i + 1) for i, x in enumerate(xs)]


def integrate(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integrate([3, 1, 2, 4, 5])
    [3, 1, 2, 4, 5]
    >>> integrate([1, 2, 3])
    [1, 2, 3]
    """
    return [x * (i + 1) for i, x in enumerate(xs)]


def integrate_from_zero(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integrate_from_zero([3, 1, 2, 4, 5])
    [3, 1, 2, 4, 5]
    >>> integrate_from_zero([1, 2, 3])
    [1, 2, 3]
    """
    return [x * i for i, x in enumerate(xs)]


def integrate_from_zero_to_x(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integrate_from_zero_to_x([3, 1, 2, 4, 5])
    [3, 1, 2, 4, 5]
    >>> integrate_from_zero_to_x([1, 2, 3])
    [1, 2, 3]
    """
    return [x * (i + 1) for i, x in enumerate(xs)]


def integrate_from_x_to_x_plus_1(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integrate_from_x_to_x_plus_1([3, 1, 2, 4, 5])
    [3, 1, 2, 4, 5]
    >>> integrate_from_x_to_x_plus_1([1, 2, 3])
    [1, 2, 3]
    """
    return [x * (i + 1) for i, x in enumerate(xs)]


def integrate_from_x_to_x_plus_2(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integrate_from_x_to_x_plus_2([3, 1, 2, 4, 5])
    [3, 1, 2, 4,