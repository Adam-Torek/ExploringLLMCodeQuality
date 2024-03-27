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

def modpow(base: int, exponent: int, modulus: int) -> int:
    """Return base^exponent modulo modulus (be aware of numerics).
    >>> modpow(3, 5, 101)
    1
    >>> modpow(1101, 101, 101)
    2
    >>> modpow(0, 101, 101)
    1
    >>> modpow(3, 11, 101)
    8
    >>> modpow(100, 101, 101)
    1
    """

def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b (be aware of numerics).
    >>> gcd(3, 5)
    1
    >>> gcd(1101, 101)
    1
    >>> gcd(0, 101)
    101
    >>> gcd(3, 11)
    1
    >>> gcd(100, 101)
    1
    """

def lcm(a: int, b: int) -> int:
    """Return the least common multiple of a and b (be aware of numerics).
    >>> lcm(3, 5)
    15
    >>> lcm(1101, 101)
    1001
    >>> lcm(0, 101)
    101
    >>> lcm(3, 11)
    33
    >>> lcm(100, 101)
    1000
    """

def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise.
    >>> is_prime(3)
    True
    >>> is_prime(5)
    True
    >>> is_prime(7)
    True
    >>> is_prime(11)
    False
    >>> is_prime(100)
    True
    """

def factorize(n: int) -> List[int]:
    """Return a list of prime factors of n.
    >>> factorize(3)
    [3]
    >>> factorize(5)
    [5]
    >>> factorize(7)
    [7]
    >>> factorize(11)
    [11]
    >>> factorize(100)
    [2, 5, 5]
    """

def prime_factors(n: int) -> List[int]:
    """Return a list of prime factors of n.
    >>> prime_factors(3)
    [3]
    >>> prime_factors(5)
    [5]
    >>> prime_factors(7)
    [7]
    >>> prime_factors(11)
    [11]
    >>> prime_factors(100)
    [2, 5, 5]
    """

def prime_factorization(n: int) -> List[Tuple[int, int]]:
    """Return a list of tuples (prime, exponent) of prime factors of n.
    >>> prime_factorization(3)
    [(3, 1)]
    >>> prime_factorization(5)
    [(5, 1)]
    >>> prime_factorization(7)
    [(7, 1)]
    >>> prime_factorization(11)
    [(11, 1)]
    >>> prime_factorization(100)
    [(2, 2), (5, 1)]
    """

def is_perfect_square(n: int) -> bool:
    """Return True if n is a perfect square, False otherwise.
    >>> is_perfect_square(9)
    True
    >>> is_perfect_square(16)
    True
    >>> is_perfect_square(25)
    True
    >>> is_perfect_square(36)
    False
    >>> is_perfect_square(49)
    False
    """

def is_square(n: int) -> bool:
    """Return True if n is a square, False otherwise.
    >>> is_square(9)
    False
    >>> is_square(16)
    True
    >>> is_square(25)
    True