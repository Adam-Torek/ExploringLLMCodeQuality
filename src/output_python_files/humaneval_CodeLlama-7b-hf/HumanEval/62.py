def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [x * (len(xs) - i) for i, x in enumerate(xs)]


def integrate(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integrate([3, 1, 2, 4, 5])
    [3, 1, 2, 4, 5]
    >>> integrate([1, 2, 3])
    [1, 2, 3]
    """
    return [x / (i + 1) for i, x in enumerate(xs)]


def integrate_and_derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integrate_and_derivative([3, 1, 2, 4, 5])
    [3, 1, 2, 4, 5]
    >>> integrate_and_derivative([1, 2, 3])
    [1, 2, 3]
    """
    return [x / (i + 1) for i, x in enumerate(xs)]


def integrate_and_derivative_2(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integrate_and_derivative_2([3, 1, 2, 4, 5])
    [3, 1, 2, 4, 5]
    >>> integrate_and_derivative_2([1, 2, 3])
    [1, 2, 3]
    """
    return [x / (i + 1) for i, x in enumerate(xs)]


def integrate_and_derivative_3(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integrate_and_derivative_3([3, 1, 2, 4, 5])
    [3, 1, 2, 4, 5]
    >>> integrate_and_derivative_3([1, 2, 3])
    [1, 2, 3]
    """
    return [x / (i + 1) for i, x in enumerate(xs)]


def integrate_and_derivative_4(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integrate_and_derivative_4([3, 1, 2, 4, 5])
    [3, 1, 2, 4, 5]
    >>> integrate_and_derivative_4([1, 2, 3])
    [1, 2, 3]
    """
    return [x / (i + 1) for i, x in enumerate(xs)]


def integrate_and_derivative_5(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1