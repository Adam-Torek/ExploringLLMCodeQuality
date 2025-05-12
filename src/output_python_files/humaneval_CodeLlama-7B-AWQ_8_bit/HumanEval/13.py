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


def is_perfect_square(n: int) -> bool:
    """ Return True if n is a perfect square, otherwise return False
    >>> is_perfect_square(3)
    False
    >>> is_perfect_square(4)
    True
    >>> is_perfect_square(10)
    False
    """
    return is_square(sqrt(n))


def is_square(n: float) -> bool:
    """ Return True if n is a square, otherwise return False
    >>> is_square(3)
    False
    >>> is_square(4)
    True
    >>> is_square(10)
    False
    """
    return n == int(n)


def is_prime_power(n: int) -> bool:
    """ Return True if n is a prime power, otherwise return False
    >>> is_prime_power(3)
    True
    >>> is_prime_power(4)
    False
    >>> is_prime_power(10)
    False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if not is_prime(n):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_power_with_exponent(n: int, e: int) -> bool:
    """ Return True if n is a prime power with exponent e, otherwise return False
    >>> is_prime_power_with_exponent(3, 2)
    False
    >>> is_prime_power_with_exponent(4, 2)
    True
    >>> is_prime_power_with_exponent(10, 2)
    False
    """
    if n < 2:
        return False
    if n == 2:
        return e == 2
    if not is_prime(n):
        return False
    if e < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_power_with_exponent_and_base(n: int, e: int, b: int) -> bool:
    """ Return True if n is a prime power with exponent e and base b, otherwise return False
    >>> is_prime_power_with_exponent_and_base(3, 2, 3)
    False
    >>> is_prime_power_with_exponent_and_base(4, 2, 2)
    True
    >>> is_prime_power_with_exponent_and_base(10, 2, 5)
    False
    """
    if n < 2:
        return False
    if n == 2:
        return e == 2 and b == 2
    if not is_prime(n):
        return False
    if e < 2:
        return False