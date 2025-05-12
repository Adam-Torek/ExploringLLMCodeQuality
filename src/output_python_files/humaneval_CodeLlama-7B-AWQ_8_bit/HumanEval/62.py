def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [x * (len(xs) - 1 - i) for i, x in enumerate(xs[1:])]


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


def integrate(f: list, a: float, b: float):
    """ f is a polynomial.
    Return the integral of f from a to b.
    >>> integrate([1, 2, 3], 0, 1)
    1.0
    >>> integrate([1, 2, 3], 0, 2)
    5.0
    >>> integrate([1, 2, 3], 1, 2)
    4.0
    >>> integrate([1, 2, 3], 1, 3)
    7.0
    """
    return sum(f * [x for x in range(a, b + 1)])


def integrate_simpson(f: list, a: float, b: float):
    """ f is a polynomial.
    Return the integral of f from a to b using Simpson's rule.
    >>> integrate_simpson([1, 2, 3], 0, 1)
    1.0
    >>> integrate_simpson([1, 2, 3], 0, 2)
    5.0
    >>> integrate_simpson([1, 2, 3], 1, 2)
    4.0
    >>> integrate_simpson([1, 2, 3], 1, 3)
    7.0
    """
    n = len(f)
    if n % 2 == 1:
        f = f + [0]
        n += 1
    h = (b - a) / (n - 1)
    x = a
    s = 0
    for i in range(n):
        s += f[i] * (x + h / 2)
        x += h
    return s


def integrate_trapezoid(f: list, a: float, b: float):
    """ f is a polynomial.
    Return the integral of f from a to b using trapezoid rule.
    >>> integrate_trapezoid([1, 2, 3], 0, 1)
    1.0
    >>> integrate_trapezoid([1, 2, 3], 0, 2)
    5.0
    >>> integrate_trapezoid([1, 2, 3], 1, 2)
    4.0
    >>> integrate_trapezoid([1, 2, 3], 1, 3)
    7.0
    """
    n = len(f)
    h = (b - a) / (n - 1)
    x = a
    s = 0
    for i in range(n):
        s += f[i] * (x + h / 2)
        x += h
    return s


def integrate_midpoint(f: list, a: float, b: float):
    """ f is a polynomial.
    Return the integral of f from a to b using midpoint rule.
    >>> integrate_midpoint([1, 2, 3], 0, 1)
    1.0
    >>> integrate_midpoint([1, 2, 3