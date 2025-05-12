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
    return (((1 << n) & p) - 1) % p


def modp_inv(n: int, p: int):
    """Return the modular inverse of n modulo p.
    >>> modp_inv(3, 5)
    2
    >>> modp_inv(1101, 101)
    2
    >>> modp_inv(0, 101)
    1
    >>> modp_inv(3, 11)
    8
    >>> modp_inv(100, 101)
    1
    """
    if p == 1:
        return 0
    if n == 1:
        return 1
    if n == p - 1:
        return 1
    if n % p == 0:
        return 0
    x = 0
    y = 1
    while True:
        q = n // p
        t = p
        p = n % p
        n = t
        t = q
        q = n // p
        n = t - q * x
        if n % p == 0:
            x = (x + y) % p
            break
        y = (y * t) % p
    return x


def modp_mul_inv(n: int, p: int):
    """Return n * modp_inv(n, p).
    >>> modp_mul_inv(3, 5)
    15
    >>> modp_mul_inv(1101, 101)
    1100
    >>> modp_mul_inv(0, 101)
    1
    >>> modp_mul_inv(3, 11)
    22
    >>> modp_mul_inv(100, 101)
    100
    """
    if n == 1:
        return 1
    if n % p == 0:
        return 0
    x = 0
    y = 1
    while True:
        q = n // p
        t = p
        p = n % p
        n = t
        t = q
        q = n // p
        n = t - q * x
        if n % p == 0:
            x = (x + y) % p
            break
        y = (y * t) % p
    return (x * n) % p


def modp_pow(n: int, p: int):
    """Return n**p modulo p.
    >>> modp_pow(3, 5)
    243
    >>> modp_pow(1101, 101)
    1100
    >>> modp_pow(0, 101)
    1
    >>> modp_pow(3, 11)
    597
    >>> modp_pow(100, 101)
    1
    """
    if p == 1:
        return n
    if p % 2 == 1:
        return modp_pow(modp_pow(n, p // 2), 2)
    r = modp_pow(n, p // 2)
    return modp_mul_inv(r, p) * r


def modp_gcd(n: int, p: int):
    """Return the greatest common divisor of n and p.
    >>> modp_gcd(3, 5)
    1
    >>> modp_gcd(1101, 101)
    1
    >>> modp_gcd(0