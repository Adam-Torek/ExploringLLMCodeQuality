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


def integral(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integral([3, 1, 2, 4, 5])
    [0, 3, 1, 2, 4, 5]
    >>> integral([1, 2, 3])
    [0, 1, 2, 3]
    """
    return [0] + xs


def interpolate(xs: list, ys: list):
    """ xs and ys are lists of numbers.
    Return a list of coefficients of a polynomial that interpolates
    the given points.
    >>> interpolate([1, 2, 3], [4, 5, 6])
    [4, 1, 1, 0, 0, 0]
    >>> interpolate([1, 2, 3], [1, 4, 9])
    [1, 3, 3, 1]
    """
    xs = [1] + xs
    ys = [0] + ys
    return [((xs[i + 1] - xs[i]) / (ys[i + 1] - ys[i])) for i in range(len(xs) - 1)]


def lagrange_interpolate(xs: list, ys: list):
    """ xs and ys are lists of numbers.
    Return a list of coefficients of a polynomial that interpolates
    the given points.
    >>> lagrange_interpolate([1, 2, 3], [4, 5, 6])
    [4, 1, 1, 0, 0, 0]
    >>> lagrange_interpolate([1, 2, 3], [1, 4, 9])
    [1, 3, 3, 1]
    """
    xs = [1] + xs
    ys = [0] + ys
    return [
        sum(
            [
                (ys[i] * (xs[j] - xs[i]) / (xs[j] - xs[i]))
                for i in range(len(xs))
                if i != j
            ]
        )
        for j in range(len(xs))
    ]


def lagrange_interpolate_extrapolate(xs: list, ys: list):
    """ xs and ys are lists of numbers.
    Return a list of coefficients of a polynomial that interpolates
    the given points.
    >>> lagrange_interpolate_extrapolate([1, 2, 3], [4, 5, 6])
    [4, 1, 1, 0, 0, 0]
    >>> lagrange_interpolate_extrapolate([1, 2, 3], [1, 4, 9])
    [1, 3, 3, 1]
    """
    xs = [1] + xs
    ys = [0] + ys
    return [
        sum(
            [
                (ys[i] * (xs[j] - xs[i]) / (xs[j] - xs[i]))
                for i in range(len(xs))
                if i != j
            ]
        )
        for j in range(len(xs) + 1)
    ]


def lagrange