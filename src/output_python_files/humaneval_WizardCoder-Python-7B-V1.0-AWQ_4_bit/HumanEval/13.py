def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)


def least_common_multiple(a: int, b: int) -> int:
    """ Return a least common multiple of two integers a and b
    >>> least_common_multiple(3, 5)
    15
    >>> least_common_multiple(25, 15)
    75
    """
    return a * b // greatest_common_divisor(a, b)

def is_prime(n: int) -> bool:
    """ Return True if n is a prime number, False otherwise
    >>> is_prime(7)
    True
    >>> is_prime(12)
    False
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n: int) -> List[int]:
    """ Return a list of prime factors of a positive integer n
    >>> prime_factors(12)
    [2, 2, 3]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def prime_factorization(n: int) -> str:
    """ Return a string of prime factors of a positive integer n
    >>> prime_factorization(12)
    '2*2*3'
    """
    return '*'.join(str(x) for x in prime_factors(n))

def is_perfect_square(n: int) -> bool:
    """ Return True if n is a perfect square, False otherwise
    >>> is_perfect_square(9)
    True
    >>> is_perfect_square(10)
    False
    """
    return int(n**0.5)**2 == n

def is_prime_power(n: int) -> bool:
    """ Return True if n is a prime power, False otherwise
    >>> is_prime_power(12)
    False
    >>> is_prime_power(15)
    True
    """
    if is_prime(n):
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_product(n: int) -> bool:
    """ Return True if n is a product of primes, False otherwise
    >>> is_prime_product(12)
    True
    >>> is_prime_product(24)
    False
    """
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and not is_prime(i):
            return False
    return True

def is_prime_sum(n: int) -> bool:
    """ Return True if n is a sum of primes, False otherwise
    >>> is_prime_sum(12)
    True
    >>> is_prime_sum(24)
    False
    """
    for i in range(2, int(n**0.5) + 1):
        if n - i > 0 and is_prime(i) and is_prime_product(n - i):
            return True
    return False

def is_prime_cube(n: int) -> bool:
    """ Return True if