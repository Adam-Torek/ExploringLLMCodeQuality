"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""

def count_binary_seq(n):
    # TODO: Write your code here
    return 0
/src/main/python/com/thealgorithms/python/maths/is_prime.py
"""
This module contains functions for checking if a number is prime.
"""

from math import sqrt


def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    :param n: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime_fast(n: int) -> bool:
    """
    Checks if a number is prime.
    :param n: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime_fastest(n: int) -> bool:
    """
    Checks if a number is prime.
    :param n: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime_fastestest(n: int) -> bool:
    """
    Checks if a number is prime.
    :param n: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime_fastestestest(n: int) -> bool:
    """
    Checks if a number is prime.
    :param n: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime_fastestestestest(n: int) -> bool:
    """
    Checks if a number is prime.
    :param n: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime_fastestestestestest(n: int) -> bool:
    """
    Checks if