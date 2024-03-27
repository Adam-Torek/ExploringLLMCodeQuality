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
    15
    >>> evaluate([1, 2, 3], 2)
    10
    """

def simplify(xs: list):
    """ xs represent coefficients of a polynomial.
    Simplify the polynomial by removing terms that are zero.
    >>> simplify([3, 1, 0, 4, 5])
    [3, 4, 5]
    >>> simplify([1, 2, 3, 0, 4, 5])
    [1, 2, 3, 4, 5]
    """

def factor(xs: list):
    """ xs represent coefficients of a polynomial.
    Factor the polynomial into its prime factors.
    >>> factor([3, 1, 2, 4, 5])
    [(2, 1), (3, 1), (5, 1)]
    >>> factor([1, 2, 3])
    [(1, 1), (2, 1), (3, 1)]
    """

def gcd(a: int, b: int):
    """ Compute the greatest common divisor of a and b.
    >>> gcd(12, 18)
    6
    >>> gcd(12, 12)
    12
    """

def lcm(a: int, b: int):
    """ Compute the least common multiple of a and b.
    >>> lcm(12, 18)
    36
    >>> lcm(12, 12)
    120
    """

def is_prime(n: int):
    """ Check if n is prime.
    >>> is_prime(12)
    True
    >>> is_prime(13)
    False
    """

def prime_factors(n: int):
    """ Compute the prime factors of n.
    >>> prime_factors(12)
    [(2, 2), (3, 1)]
    >>> prime_factors(13)
    [(2, 1), (3, 1)]
    """

def is_square(n: int):
    """ Check if n is a perfect square.
    >>> is_square(16)
    True
    >>> is_square(17)
    False
    """

def square_root(n: int):
    """ Compute the square root of n.
    >>> square_root(16)
    4
    >>> square_root(17)
    4
    """

def is_prime_power(n: int):
    """ Check if n is a prime power.
    >>> is_prime_power(12)
    True
    >>> is_prime_power(13)
    False
    """

def prime_power(n: int):
    """ Compute the prime power of n.
    >>> prime_power(12)
    (2, 2)
    >>> prime_power(13)
    (2, 1)
    """

def is_perfect_square(n: int):
    """ Check if n is a perfect square.
    >>> is_perfect_square(16)
    True
    >>> is_perfect_square(17)
    False
    """

def perfect_square(n: int):
    """ Compute the perfect square of n.
    >>> perfect_square(16)
    4
    >>> perfect_square(17)
    4
    """

def is_perfect_power(n: int):
    """ Check if n is a perfect power.
    >>> is_perfect_power(16)
    True
    >>> is_perfect_power(17)
    False
    """

def perfect_power(n: int):
    """ Compute the perfect power of n.
    >>> perfect_power(16)
    (2, 4)
    >>> perfect_power(17)
    (2, 3)
    """

def is_perfect_cube(n: int