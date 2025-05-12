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


def modp_sqrt(n: int, p: int):
    """Return the square root of n modulo p.
    >>> modp_sqrt(3, 5)
    2
    >>> modp_sqrt(1101, 101)
    100
    >>> modp_sqrt(0, 101)
    1
    >>> modp_sqrt(3, 11)
    8
    >>> modp_sqrt(100, 101)
    1
    """
    return pow(n, (p + 1) // 4, p)


def modp_sqrt_inv(n: int, p: int):
    """Return the inverse of the square root of n modulo p.
    >>> modp_sqrt_inv(3, 5)
    2
    >>> modp_sqrt_inv(1101, 101)
    100
    >>> modp_sqrt_inv(0, 101)
    1
    >>> modp_sqrt_inv(3, 11)
    8
    >>> modp_sqrt_inv(100, 101)
    1
    """
    return pow(n, (p - 1) // 4, p)


def modp_pow(n: int, e: int, p: int):
    """Return n^e modulo p.
    >>> modp_pow(3, 5, 5)
    3
    >>> modp_pow(1101, 101, 101)
    1
    >>> modp_pow(0, 101, 101)
    1
    >>> modp_pow(3, 11, 11)
    8
    >>> modp_pow(100, 101, 101)
    1
    """
    return pow(n, e, p)


def modp_inv_pow(n: int, e: int, p: int):
    """Return the inverse of n^e modulo p.
    >>> modp_inv_pow(3, 5, 5)
    3
    >>> modp_inv_pow(1101, 101, 101)
    1
    >>> modp_inv_pow(0, 101, 101)
    1
    >>> modp_inv_pow(3, 11, 11)
    8
    >>> modp_inv_pow(100, 101, 101)
    1
    """
    return pow(n, (p - 2) // e, p)


def modp_sqrt_pow(n: int, e: int, p: int):
    """Return the square root of n^e modulo p.
    >>> modp_sqrt_pow(3, 5, 5)
    3
    >>> modp_sqrt_pow(1