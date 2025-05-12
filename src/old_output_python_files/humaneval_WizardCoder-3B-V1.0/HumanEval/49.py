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
    1
    >>> modpow(0, 101, 101)
    0
    >>> modpow(3, 11, 101)
    1
    >>> modpow(100, 101, 101)
    1
    """

def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b (be aware of numerics).
    >>> gcd(12, 18)
    6
    >>> gcd(100, 200)
    100
    >>> gcd(100, 0)
    100
    >>> gcd(0, 100)
    100
    """

def lcm(a: int, b: int) -> int:
    """Return the least common multiple of a and b (be aware of numerics).
    >>> lcm(12, 18)
    36
    >>> lcm(100, 200)
    2000
    >>> lcm(100, 0)
    0
    >>> lcm(0, 100)
    0
    """

def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise.
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(100)
    True
    >>> is_prime(0)
    False
    """

def factorize(n: int) -> List[int]:
    """Return a list of prime factors of n.
    >>> factorize(11)
    [11]
    >>> factorize(12)
    [2, 2]
    >>> factorize(100)
    [2, 5, 5]
    >>> factorize(0)
    []
    """

def prime_factors(n: int) -> List[int]:
    """Return a list of prime factors of n.
    >>> prime_factors(11)
    [11]
    >>> prime_factors(12)
    [2, 2]
    >>> prime_factors(100)
    [2, 5, 5]
    >>> prime_factors(0)
    []
    """

def prime_factorization(n: int) -> List[Tuple[int, int]]:
    """Return a list of tuples (prime, power) of prime factors of n.
    >>> prime_factorization(11)
    [(11, 1)]
    >>> prime_factorization(12)
    [(2, 2), (2, 1)]
    >>> prime_factorization(100)
    [(2, 2), (5, 1), (5, 1)]
    >>> prime_factorization(0)
    []
    """

def is_perfect_square(n: int) -> bool:
    """Return True if n is a perfect square, False otherwise.
    >>> is_perfect_square(16)
    True
    >>> is_perfect_square(17)
    False
    >>> is_perfect_square(100)
    True
    >>> is_perfect_square(0)
    False
    """

def is_square(n: int) -> bool:
    """Return True if n is a square, False otherwise.
    >>> is_square(16)
    False
    >>> is_square(17)
    True
    >>> is_square(100)
    False
    >>> is_square(0)
    False
    """

def is_prime_power(n: int) -> bool:
    """Return True if n is a prime power, False otherwise.
    >>> is_prime_power(16)
    False
    >>> is_prime_power(17)
    True
    >>> is_prime_power