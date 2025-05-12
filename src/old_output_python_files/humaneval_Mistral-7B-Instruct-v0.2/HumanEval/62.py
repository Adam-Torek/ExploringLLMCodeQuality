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
        return [0]
    else:
        return [xs[i+1] for i in range(len(xs)-1)]

def integrate(xs: list, constant: float = 0):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial with given constant.
    >>> integrate([3, 1, 2, 4, 5])
    15/3 * x^4 + 2 * x^3 + 4/3 * x^2 + x
    >>> integrate([1, 2, 3])
    1/2 * x^2 + 3/2 * x + constant
    """
    if len(xs) == 0:
        return "0"
    elif len(xs) == 1:
        return str(xs[0] * x + constant)
    else:
        return "(" + str(xs[0]/(2*len(xs))*x**(len(xs))) + ")" + \
               " + " + str(sum([xs[i]*integrate(derivative(xs[:i])) for i in range(1,len(xs))])) + \
               " + " + str(constant)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(integrate([3, 1, 2, 4, 5]))
    print(integrate([1, 2, 3]))
    print(integrate([1, 2, 3], 1))