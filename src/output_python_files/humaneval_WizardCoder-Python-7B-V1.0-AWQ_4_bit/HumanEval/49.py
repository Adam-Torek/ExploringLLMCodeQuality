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
    def egcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return (b, 0, 1)
        else:
            gcd, x, y = egcd(b % a, a)
            return (gcd, y - (b // a) * x, x)

    return egcd(a, p)[2] % p

def modpow(base: int, exp: int, p: int) -> int:
    """Return base^exp modulo p.
    >>> modpow(2, 3, 5)
    2
    >>> modpow(2, 10, 5)
    3
    >>> modpow(7, 101, 11)
    8
    """
    return (base ** exp) % p

def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(10)
    False
    >>> is_prime(7919)
    True
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b.
    >>> gcd(12, 8)
    4
    >>> gcd(17, 21)
    1
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a: int, b: int) -> int:
    """Return the least common multiple of a and b.
    >>> lcm(12, 8)
    24
    >>> lcm(17, 21)
    34
    """
    return a * b // gcd(a, b)

def crt(a: int, m: int, b: int, n: int) -> int:
    """Return the Chinese Remainder Theorem solution x.
    >>> crt(2, 3, 5, 7)
    13
    >>> crt(1, 3, 7, 11)
    1
    """
    M = m * n
    M_inv = modinv(M, n)
    return (a * modpow(m, b, n) * M_inv * n) % M

def crt_list(a: List[int], m: List[int], n: List[int]) -> List[int]:
    """Return the Chinese Remainder Theorem solution for a list of moduli.
    >>> crt_list([2, 3], [3, 7], [5, 11])
    [13, 1]
    """
    M = prod(n)
    M_inv = modinv(M, prod(m))
    return [(a[i] * modpow(m[i], b[i], M) * M_inv * lcm(m[i], n[i]) * M // m[i]) % M