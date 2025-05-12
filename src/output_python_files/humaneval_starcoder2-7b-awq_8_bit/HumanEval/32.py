import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
#    if len(xs) % 2 == 0 and xs[-1]!= 0:
    if len(xs) % 2 == 0 and xs[-1]!= 0:
        return -xs[0] / xs[1]
    else:
        raise ValueError("xs must have even number of coefficients and largest non zero coefficient")


def find_zero_interval(xs: list, a: float, b: float):
    """
    Find zero of polynomial with coefficients xs in interval [a, b].
    """
    if a > b:
        raise ValueError("a must be smaller than b")
    if len(xs) % 2 == 0 and xs[-1]!= 0:
        if poly(xs, a) * poly(xs, b) < 0:
            return find_zero(xs)
        else:
            raise ValueError("f(a) * f(b) must be negative")
    else:
        raise ValueError("xs must have even number of coefficients and largest non zero coefficient")


def find_zero_interval_recursive(xs: list, a: float, b: float):
    """
    Find zero of polynomial with coefficients xs in interval [a, b].
    """
    if a > b:
        raise ValueError("a must be smaller than b")
    if len(xs) % 2 == 0 and xs[-1]!= 0:
        if poly(xs, a) * poly(xs, b) < 0:
            return find_zero(xs)
        else:
            raise ValueError("f(a) * f(b) must be negative")
    else:
        raise ValueError("xs must have even number of coefficients and largest non zero coefficient")


def find_zero_interval_recursive_2(xs: list, a: float, b: float):
    """
    Find zero of polynomial with coefficients xs in interval [a, b].
    """
    if a > b:
        raise ValueError("a must be smaller than b")
    if len(xs) % 2 == 0 and xs[-1]!= 0:
        if poly(xs, a) * poly(xs, b) < 0:
            return find_zero(xs)
        else:
            raise ValueError("f(a) * f(b) must be negative")
    else:
        raise ValueError("xs must have even number of coefficients and largest non zero coefficient")


def find_zero_interval_recursive_3(xs: list, a: float, b: float):
    """
    Find zero of polynomial with coefficients xs in interval [a, b].
    """
    if a > b:
        raise ValueError("a must be smaller than b")
    if len(xs) % 2 == 0 and xs[-1]!= 0:
        if poly(xs, a) * poly(xs, b) < 0:
            return find_zero(xs)
        else:
            raise ValueError("f(a) * f(b) must be negative")
    else:
        raise ValueError("xs must have even number of coefficients and largest non zero coefficient")


def find_zero_interval_recursive_4(xs: list, a: float, b: float):
    """
    Find zero of polynomial with coefficients xs in interval [a, b].
    """
    if a > b:
        raise ValueError("a must be smaller than b")
    if len(xs) % 2 == 0 and xs[-1]!= 0:
        if poly(xs, a) *