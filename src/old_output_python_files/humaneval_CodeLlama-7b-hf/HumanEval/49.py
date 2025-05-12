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
    >>> modinv(2, 101)
    100
    >>> modinv(3, 11)
    8
    >>> modinv(100, 101)
    1
    """
    return pow(a, p - 2, p)


def modmul(a: int, b: int, p: int):
    """Return the modular product of a and b modulo p.
    >>> modmul(2, 3, 101)
    6
    >>> modmul(100, 101, 101)
    1
    >>> modmul(100, 101, 11)
    8
    """
    return (a * b) % p


def modadd(a: int, b: int, p: int):
    """Return the modular sum of a and b modulo p.
    >>> modadd(2, 3, 101)
    5
    >>> modadd(100, 101, 101)
    1
    >>> modadd(100, 101, 11)
    9
    """
    return (a + b) % p


def modsub(a: int, b: int, p: int):
    """Return the modular difference of a and b modulo p.
    >>> modsub(2, 3, 101)
    99
    >>> modsub(100, 101, 101)
    1
    >>> modsub(100, 101, 11)
    9
    """
    return (a - b) % p


def moddiv(a: int, b: int, p: int):
    """Return the modular division of a and b modulo p.
    >>> moddiv(2, 3, 101)
    100
    >>> moddiv(100, 101, 101)
    1
    >>> moddiv(100, 101, 11)
    9
    """
    return modmul(a, modinv(b, p), p)


def modpow(a: int, b: int, p: int):
    """Return the modular exponentiation of a and b modulo p.
    >>> modpow(2, 3, 101)
    8
    >>> modpow(100, 101, 101)
    1
    >>> modpow(100, 101, 11)
    9
    """
    return pow(a, b, p)


def modsqrt(a: int, p: int):
    """Return the modular square root of a modulo p.
    >>> modsqrt(2, 101)
    100
    >>> modsqrt(3, 11)
    8
    >>> modsqrt(100, 101)
    1
    """
    if a == 0:
        return 0
    if a == 1:
        return 1
    if p == 2:
        return 1
    if p % 4 == 3:
        return modpow(a, (p + 1) // 4, p)
    if p % 8 == 5:
        return modpow(a, (p - 1) // 4, p)
    if p % 8 == 7:
        return modpow(a, (p + 3) // 8, p)
    if p % 8 ==