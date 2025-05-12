def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

def evaluate(xs: list, x: float):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Evaluate the polynomial at x.
    >>> evaluate([3, 1, 2, 4, 5], 2)
    13
    >>> evaluate([1, 2, 3], 2)
    10
    """

def differentiate(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Differentiate the polynomial in the same form.
    >>> differentiate([3, 1, 2, 4, 5])
    [1, 4, 12, 20, 0]
    >>> differentiate([1, 2, 3])
    [2, 6, 0]
    """

def simplify(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Simplify the polynomial in the same form.
    >>> simplify([3, 1, 2, 4, 5])
    [1, 4, 12, 20, 0]
    >>> simplify([1, 2, 3])
    [2, 6, 0]
    """

def factor(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Factor the polynomial in the same form.
    >>> factor([3, 1, 2, 4, 5])
    [1, 4, 12, 20, 0]
    >>> factor([1, 2, 3])
    [2, 6, 0]
    """

def expand(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Expand the polynomial in the same form.
    >>> expand([3, 1, 2, 4, 5])
    [1, 4, 12, 20, 0]
    >>> expand([1, 2, 3])
    [1, 2, 3, 0]
    """

def cancel(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Cancel the polynomial in the same form.
    >>> cancel([3, 1, 2, 4, 5])
    [1, 4, 12, 20, 0]
    >>> cancel([1, 2, 3])
    [1, 2, 3, 0]
    """

def cancel_common_factors(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Cancel common factors of the polynomial in the same form.
    >>> cancel_common_factors([3, 1, 2, 4, 5])
    [1, 4, 12, 20, 0]
    >>> cancel_common_factors([1, 2, 3])
    [1, 2, 3, 0]
    """

def cancel_exponents(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Cancel exponents of the polynomial in the same form.
    >>> cancel_exponents([3, 1, 2, 4, 5])
    [1, 4, 12, 20, 0]
    >>> cancel_exponents([1, 2, 3])
    [1, 2, 3, 0]
    """

def cancel_multiplicative