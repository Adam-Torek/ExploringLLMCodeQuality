from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors


def is_prime(n: int) -> bool:
    """ Return True if given integer is prime, False otherwise.
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(13)
    True
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_perfect_square(n: int) -> bool:
    """ Return True if given integer is a perfect square, False otherwise.
    >>> is_perfect_square(1)
    True
    >>> is_perfect_square(4)
    True
    >>> is_perfect_square(16)
    True
    >>> is_perfect_square(17)
    False
    """
    return n ** 0.5 % 1 == 0


def is_palindrome(n: int) -> bool:
    """ Return True if given integer is a palindrome, False otherwise.
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(12345)
    False
    """
    return str(n) == str(n)[::-1]


def is_pandigital(n: int) -> bool:
    """ Return True if given integer is a pandigital, False otherwise.
    >>> is_pandigital(123456789)
    True
    >>> is_pandigital(12345678)
    False
    """
    return str(n) == "123456789"


def is_pandigital_prime(n: int) -> bool:
    """ Return True if given integer is a pandigital prime, False otherwise.
    >>> is_pandigital_prime(123456789)
    True
    >>> is_pandigital_prime(12345678)
    False
    """
    return is_pandigital(n) and is_prime(n)


def is_semiprime(n: int) -> bool:
    """ Return True if given integer is a semiprime, False otherwise.
    >>> is_semiprime(12)
    True
    >>> is_semiprime(13)
    False
    """
    return is_prime(n) or is_prime(n - 1)


def is_semiprime_prime(n: int) -> bool:
    """ Return True if given integer is a semiprime prime, False otherwise.
    >>> is_semiprime_prime(12)
    True
    >>> is_semiprime_prime(13)
    False
    """
    return is_prime(n) and is_prime(n - 1)


def is_prime_power(n: int) -> bool:
    """ Return True if given integer is a prime power, False otherwise.
    >>> is_prime_power(1)
    True
    >>> is_prime_