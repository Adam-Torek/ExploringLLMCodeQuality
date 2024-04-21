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


def multiply(xs: list, ys: list):
    """ xs and ys represent coefficients of two polynomials.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    ys[0] + ys[1] * x + ys[2] * x^2 + ....
     Return coefficients of their product in the same form.
    >>> multiply([3, 1, 2, 4, 5], [1, 2, 3])
    [3, 10, 12, 20, 25]
    >>> multiply([1, 2, 3], [1, 2, 3])
    [1, 4, 9]
    """
    return [sum(x * y for x, y in zip(xs, ys)) for y in ys]


def divide(xs: list, ys: list):
    """ xs and ys represent coefficients of two polynomials.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    ys[0] + ys[1] * x + ys[2] * x^2 + ....
     Return coefficients of their quotient in the same form.
    >>> divide([3, 1, 2, 4, 5], [1, 2, 3])
    [3, 1, 2, 4, 5]
    >>> divide([1, 2, 3], [1, 2, 3])
    [1, 0, 0]
    """
    return [x / y for x, y in zip(xs, ys)]


def evaluate(xs: list, x: float):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return value of this polynomial at x.
    >>> evaluate([3, 1, 2, 4, 5], 2)
    35
    >>> evaluate([1, 2, 3], 2)
    10
    """
    return sum(x * (x ** i) for i, x in enumerate(xs))


def roots(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return roots of this polynomial.
    >>> roots([3, 1, 2, 4, 5])
    [1.0, 2.0]
    >>> roots([1, 2, 3])
    []
    """
    if len(xs) == 1:
        return []
    if len(xs) == 2:
        return [-xs[0] / xs[1]]
    if len(xs) == 3:
        return [
            (-xs[0] + (xs[2] ** 2 - xs[1] ** 2) ** 0.5) / xs[1],
            (-xs[0] - (xs[2] ** 2 - xs[1] ** 2) ** 0.5