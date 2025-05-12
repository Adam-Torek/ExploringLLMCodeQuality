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
    return 2 ** n % p


def modinv(a: int, p: int) -> int:
    """Return the modular inverse of a modulo p.
    >>> modinv(2, 5)
    3
    >>> modinv(7, 11)
    8
    >>> modinv(101, 101)
    1
    """
    if a == 0:
        return 0
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = egcd(b % a, a)
            return (g, y - (b // a) * x, x)
    return (modp(egcd(a, p)[2] + p) % p) if egcd(a, p)[0] == 1 else None

def modpow(base: int, exponent: int, modulus: int) -> int:
    """Return base^exponent modulo modulus.
    >>> modpow(2, 10, 13)
    8
    >>> modpow(3, 3, 11)
    9
    """
    return (base % modulus) ** exponent % modulus

def modsqrt(n: int, p: int) -> int:
    """Return the square root of n modulo p.
    >>> modsqrt(2, 11)
    10
    >>> modsqrt(3, 11)
    5
    """
    if modpow(n, (p - 1) // 2, p) != 1:
        return None
    def legendre_symbol(a, p):
        return modpow(a, (p - 1) // 2, p)
    if legendre_symbol(n, p) != p - 1:
        return None
    def tonelli_shanks(n, p):
        if p % 2 == 3 or p == 2:
            return modpow(n, (p + 1) // 4, p)
        else:
            return pow(n, (p + 1) // 4, p)
    return tonelli_shanks(2, p)

def modsqrt_iter(n: int, p: int) -> int:
    """Return the square root of n modulo p using the iterative algorithm.
    >>> modsqrt_iter(2, 11)
    10
    >>> modsqrt_iter(3, 11)
    5
    """
    if modpow(n, (p - 1) // 2, p) != 1:
        return None
    def legendre_symbol(a, p):
        return modpow(a, (p - 1) // 2, p)
    if legendre_symbol(n, p) != p - 1:
        return None
    def tonelli_shanks_iter(n, p):
        if p % 2 == 3 or p == 2:
            return modpow(n, (p + 1) // 4, p)
        else:
            return pow(n, (p + 1) // 4, p)
    return tonelli_shanks_iter(2, p)

def modsqrt_newton(n: int, p: int) -> int:
    """Return the square root of n modulo p using the Newton's method.
    >>> modsqrt_newton(2, 11)
    10
    >>> modsqrt_newton(3, 11)
    5
    """
    if modpow(n, (p - 1) // 2, p) != 1:
        return None
    def legendre_symbol(a, p):
        return modpow(a, (p