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
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors


def is_prime(n: int) -> bool:
    """ Return True if given integer is prime, False otherwise.
    >>> is_prime(17)
    True
    >>> is_prime(18)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_perfect_square(n: int) -> bool:
    """ Return True if given integer is a perfect square, False otherwise.
    >>> is_perfect_square(16)
    True
    >>> is_perfect_square(25)
    False
    >>> is_perfect_square(1)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            if i * i == n:
                return True
    return False


def is_palindrome(n: int) -> bool:
    """ Return True if given integer is a palindrome, False otherwise.
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(12345)
    False
    >>> is_palindrome(1)
    True
    """
    if n < 10:
        return True
    for i in range(len(str(n)) // 2):
        if str(n)[i] != str(n)[-i - 1]:
            return False
    return True


def is_abundant(n: int) -> bool:
    """ Return True if given integer is an abundant number, False otherwise.
    An abundant number is a number whose sum of proper divisors is greater than the number itself.
    >>> is_abundant(12)
    True
    >>> is_abundant(13)
    False
    >>> is_abundant(1)
    False
    """
    if n < 12:
        return False
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    if sum_of_divisors > n:
        return True
    return False


def is_deficient(n: int) -> bool:
    """ Return True if given integer is a deficient number, False otherwise.
    A deficient number is a number whose sum of proper divisors is less than the number itself.
    >>> is_deficient(12)
    False
    >>> is_deficient(13)
    True
    >>> is_deficient(1)
    False
    """
    if n < 13:
        return False
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    if sum_of_divisors < n:
        return True
    return False


def is_semiperfect(n: int) -> bool:
    """ Return True if given integer is a semiperfect number, False otherwise.
    A semiperfect number is a number whose sum of proper divisors is equal to the number itself.