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
    n = len(xs) // 2
    if n % 2 == 1:
        raise ValueError("Polynomial must have even number of coefficients")
    a = xs[n - 1]
    b = 0
    for i in range(n - 1):
        b += xs[i] * xs[i + 1]
    return -b / a

def find_zeros(xs: list):
    """
    Find all the zeros of the polynomial with coefficients xs.
    >>> find_zeros([1, 2]) # f(x) = 1 + 2x
    [-1.0]
    >>> find_zeros([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    """
    n = len(xs) // 2
    if n % 2 == 1:
        raise ValueError("Polynomial must have even number of coefficients")
    a = xs[n - 1]
    b = 0
    c = 0
    for i in range(n - 1):
        b += xs[i] * xs[i + 1]
        c += xs[i] * xs[i]
    delta = b * b - 4 * a * c
    if delta < 0:
        return []
    sqrt_delta = math.sqrt(delta)
    return [(-b + sqrt_delta) / (2 * a), (-b - sqrt_delta) / (2 * a)]

def find_extrema(xs: list):
    """
    Find all the extrema of the polynomial with coefficients xs.
    >>> find_extrema([1, 2]) # f(x) = 1 + 2x
    [-1.0, 0.0]
    >>> find_extrema([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    """
    n = len(xs) // 2
    if n % 2 == 1:
        raise ValueError("Polynomial must have even number of coefficients")
    a = xs[n - 1]
    b = 0
    c = 0
    d = 0
    for i in range(n - 1):
        b += xs[i] * xs[i + 1]
        c += xs[i] * xs[i]
        d += xs[i] * xs[i] * xs[i + 1]
    delta = b * b - 4 * a * c
    if delta < 0:
        return []
    sqrt_delta = math.sqrt(delta)
    return [(-b + sqrt_delta) / (2