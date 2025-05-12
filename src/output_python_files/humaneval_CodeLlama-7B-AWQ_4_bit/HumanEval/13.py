def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a


def least_common_multiple(a: int, b: int) -> int:
    """ Return a least common multiple of two integers a and b
    >>> least_common_multiple(3, 5)
    15
    >>> least_common_multiple(25, 15)
    75
    """
    return a * b // greatest_common_divisor(a, b)


def is_prime(n: int) -> bool:
    """ Return True if n is a prime number, otherwise return False
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(10)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_number(n: int) -> bool:
    """ Return True if n is a prime number, otherwise return False
    >>> is_prime_number(3)
    True
    >>> is_prime_number(4)
    False
    >>> is_prime_number(10)
    False
    """
    return is_prime(n)


def is_prime_number_v2(n: int) -> bool:
    """ Return True if n is a prime number, otherwise return False
    >>> is_prime_number_v2(3)
    True
    >>> is_prime_number_v2(4)
    False
    >>> is_prime_number_v2(10)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_number_v3(n: int) -> bool:
    """ Return True if n is a prime number, otherwise return False
    >>> is_prime_number_v3(3)
    True
    >>> is_prime_number_v3(4)
    False
    >>> is_prime_number_v3(10)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_number_v4(n: int) -> bool:
    """ Return True if n is a prime number, otherwise return False
    >>> is_prime_number_v4(3)
    True
    >>> is_prime_number_v4(4)
    False
    >>> is_prime_number_v4(10)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_number_v5(n: int) -> bool:
    """ Return True if n is a prime number, otherwise return False
    >>> is_prime_number_v5(3)
    True
    >>> is_prime_number_v5(4)
    False
    >>> is_prime_number_v5(10)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_number_v6(n: int) -> bool:
    """ Return True if n is a prime number, otherwise return False
    >>> is_prime_number_v6(3)
    True
    >>> is_prime_number_v6(4)
    False
    >>> is_prime_number