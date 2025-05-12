import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
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
    if len(xs) % 2 == 1:
        raise ValueError("xs must have even number of coefficients")
    if xs[0] == 0:
        raise ValueError("xs must have largest non zero coefficient")
    n = len(xs)
    for i in range(n):
        if xs[i] == 0:
            xs.pop(i)
            n -= 1
    x = -xs[n] / xs[n - 1]
    return x


def find_zeros(xs: list):
    """ xs are coefficients of a polynomial.
    find_zeros find all x such that poly(x) = 0.
    find_zeros returns list of all zero points, even if there are many.
    Moreover, find_zeros only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zeros([1, 2]), 2) # f(x) = 1 + 2x
    [-0.5, 0.5]
    >>> round(find_zeros([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [-1.0, 1.0]
    """
    if len(xs) % 2 == 1:
        raise ValueError("xs must have even number of coefficients")
    if xs[0] == 0:
        raise ValueError("xs must have largest non zero coefficient")
    n = len(xs)
    for i in range(n):
        if xs[i] == 0:
            xs.pop(i)
            n -= 1
    xs.sort()
    return xs