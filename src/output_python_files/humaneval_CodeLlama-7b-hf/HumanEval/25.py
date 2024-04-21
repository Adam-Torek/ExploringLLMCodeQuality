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
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                factors.append(i)
                n = n // i
                break
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
    if n == 1:
        return False
    for i in range(2, n):
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
    if n < 0:
        return False
    for i in range(1, n + 1):
        if i * i == n:
            return True
    return False


def is_palindrome(n: int) -> bool:
    """ Return True if given integer is a palindrome, False otherwise.
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(12345)
    False
    >>> is_palindrome(123456789)
    False
    """
    if n < 0:
        return False
    if n == 0:
        return True
    if n % 10 == 0:
        return False
    if n % 10 == n // 10:
        return True
    return False


def is_abundant(n: int) -> bool:
    """ Return True if given integer is an abundant number, False otherwise.
    An abundant number is a number whose sum of proper divisors is greater than the number itself.
    >>> is_abundant(12)
    True
    >>> is_abundant(13)
    False
    >>> is_abundant(28)
    True
    >>> is_abundant(29)
    False
    """
    if n < 0:
        return False
    if n == 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return False
    if n == 3:
        return False
    if n == 4:
        return False
    if n == 5:
        return False
    if n == 6:
        return False
    if n == 7:
        return False
    if n == 8:
        return False
    if n == 9:
        return False
    if n == 10:
        return False
    if n == 11:
        return False
    if n == 12:
        return False
    if n == 13:
        return False
    if n == 14:
        return False
    if n == 15:
        return False
    if n == 16:
        return False
    if n == 17:
        return False
    if n == 18:
        return False
    if n == 19:
        return False
    if n == 20:
        return False
    if n == 21:
        return False
    if n == 22: