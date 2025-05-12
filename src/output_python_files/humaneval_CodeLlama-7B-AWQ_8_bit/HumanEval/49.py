def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    return pow(2, n, p)


def modp_inv(n: int, p: int):
    """Return the inverse of n modulo p.
    >>> modp_inv(3, 5)
    2
    >>> modp_inv(1101, 101)
    100
    >>> modp_inv(0, 101)
    1
    >>> modp_inv(3, 11)
    8
    >>> modp_inv(100, 101)
    1
    """
    return pow(n, p - 2, p)


def modp_mul(a: int, b: int, p: int):
    """Return a*b modulo p.
    >>> modp_mul(3, 5, 101)
    15
    >>> modp_mul(1101, 100, 101)
    1
    >>> modp_mul(100, 101, 101)
    1
    """
    return (a * b) % p


def modp_add(a: int, b: int, p: int):
    """Return a+b modulo p.
    >>> modp_add(3, 5, 101)
    8
    >>> modp_add(1101, 100, 101)
    1
    >>> modp_add(100, 101, 101)
    1
    """
    return (a + b) % p


def modp_sub(a: int, b: int, p: int):
    """Return a-b modulo p.
    >>> modp_sub(3, 5, 101)
    8
    >>> modp_sub(1101, 100, 101)
    1
    >>> modp_sub(100, 101, 101)
    1
    """
    return (a - b) % p


def modp_div(a: int, b: int, p: int):
    """Return a/b modulo p.
    >>> modp_div(3, 5, 101)
    15
    >>> modp_div(1101, 100, 101)
    1
    >>> modp_div(100, 101, 101)
    1
    """
    return (a * modp_inv(b, p)) % p


def modp_pow(a: int, b: int, p: int):
    """Return a^b modulo p.
    >>> modp_pow(3, 5, 101)
    15
    >>> modp_pow(1101, 100, 101)
    1
    >>> modp_pow(100, 101, 101)
    1
    """
    return pow(a, b, p)


def modp_sqrt(a: int, p: int):
    """Return the square root of a modulo p.
    >>> modp_sqrt(3, 101)
    3
    >>> modp_sqrt(1101, 101)
    1
    >>> modp_sqrt(100, 101)
    1
    """
    return pow(a, (p + 1) // 4, p)


def modp_is_square(a: int, p: int):
    """Return True if a is a square modulo p.
    >>> modp_is_square(3, 1