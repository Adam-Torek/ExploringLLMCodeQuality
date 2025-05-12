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
    100
    >>> modinv(0, 101)
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
    >>> modpow(0, 101, 101)
    1
    >>> modpow(3, 11, 11)
    8
    >>> modpow(100, 101, 101)
    1
    """
    return pow(a, n, p)


def modmul(a: int, b: int, p: int):
    """Return a*b modulo p.
    >>> modmul(3, 3, 5)
    3
    >>> modmul(1101, 1101, 101)
    1
    >>> modmul(0, 101, 101)
    1
    >>> modmul(3, 11, 11)
    8
    >>> modmul(100, 101, 101)
    1
    """
    return (a * b) % p


def modadd(a: int, b: int, p: int):
    """Return a+b modulo p.
    >>> modadd(3, 3, 5)
    3
    >>> modadd(1101, 1101, 101)
    1
    >>> modadd(0, 101, 101)
    1
    >>> modadd(3, 11, 11)
    8
    >>> modadd(100, 101, 101)
    1
    """
    return (a + b) % p


def modsub(a: int, b: int, p: int):
    """Return a-b modulo p.
    >>> modsub(3, 3, 5)
    0
    >>> modsub(1101, 1101, 101)
    0
    >>> modsub(0, 101, 101)
    0
    >>> modsub(3, 11, 11)
    8
    >>> modsub(100, 101, 101)
    0
    """
    return (a - b) % p


def moddiv(a: int, b: int, p: int):
    """Return a/b modulo p.
    >>> moddiv(3, 3, 5)
    1
    >>> moddiv(1101, 1101, 101)
    1
    >>> moddiv(0, 101, 101)
    1
    >>> moddiv(3, 11, 11)
    8
    >>> moddiv(100, 101, 101)
    1