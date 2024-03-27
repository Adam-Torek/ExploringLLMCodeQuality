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


def modinv(a: int, p: int):
    """Return the modular inverse of a modulo p.
    >>> modinv(3, 5)
    2
    >>> modinv(1101, 101)
    1
    >>> modinv(3, 11)
    8
    >>> modinv(100, 101)
    1
    """
    return pow(a, p - 2, p)


def modpow(a: int, n: int, p: int):
    """Return a^n modulo p.
    >>> modpow(3, 3, 5)
    3
    >>> modpow(1101, 1101, 101)
    1
    >>> modpow(3, 11, 11)
    8
    >>> modpow(100, 100, 101)
    1
    """
    return pow(a, n, p)


def modsqrt(a: int, p: int):
    """Return the square root of a modulo p.
    >>> modsqrt(3, 5)
    2
    >>> modsqrt(1101, 101)
    1
    >>> modsqrt(3, 11)
    8
    >>> modsqrt(100, 101)
    1
    """
    if p == 2:
        return a
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    if p % 8 == 5:
        return pow(a, (p - 1) // 4, p)
    if p % 8 == 7:
        return pow(a, (p + 3) // 4, p)
    raise ValueError("p must be a prime number")


def modsqrt_inv(a: int, p: int):
    """Return the inverse of the square root of a modulo p.
    >>> modsqrt_inv(3, 5)
    2
    >>> modsqrt_inv(1101, 101)
    1
    >>> modsqrt_inv(3, 11)
    8
    >>> modsqrt_inv(100, 101)
    1
    """
    if p == 2:
        return a
    if p % 4 == 3:
        return pow(a, (p - 1) // 4, p)
    if p % 8 == 5:
        return pow(a, (p + 3) // 4, p)
    if p % 8 == 7:
        return pow(a, (p - 1) // 4, p)
    raise ValueError("p must be a prime number")


def modsqrt_inv_sqrt(a: int, p: int):
    """Return the inverse of the square root of a modulo p.
    >>> modsqrt_inv_sqrt(3, 5)
    2
    >>> modsqrt_inv_sqrt(1101, 101)
    1
    >>> modsqrt_inv_sqrt(3, 11)
    8
    >>> modsqrt_inv_sqrt(100, 101)
    1
    """
    if p == 2:
        return a
    if p % 4 == 3:
        return pow(a, (p - 1) // 4, p)
    if p % 8 == 5:
        return pow(a, (p + 3) // 4, p)
    if p % 8 == 7:
        return pow(a, (p - 1) //