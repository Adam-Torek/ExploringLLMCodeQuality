def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b != 0:
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
    """ Return True if n is prime, otherwise return False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
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
    """ Return True if n is perfect square, otherwise return False
    >>> is_perfect_square(1)
    False
    >>> is_perfect_square(2)
    True
    >>> is_perfect_square(3)
    False
    >>> is_perfect_square(4)
    True
    >>> is_perfect_square(5)
    False
    >>> is_perfect_square(6)
    False
    >>> is_perfect_square(7)
    False
    >>> is_perfect_square(8)
    True
    >>> is_perfect_square(9)
    False
    >>> is_perfect_square(10)
    False
    """
    if n < 2:
        return False
    for i in range(1, n + 1):
        if i * i == n:
            return True
    return False


def is_perfect_cube(n: int) -> bool:
    """ Return True if n is perfect cube, otherwise return False
    >>> is_perfect_cube(1)
    False
    >>> is_perfect_cube(2)
    False
    >>> is_perfect_cube(3)
    True
    >>> is_perfect_cube(4)
    False
    >>> is_perfect_cube(5)
    False
    >>> is_perfect_cube(6)
    False
    >>> is_perfect_cube(7)
    False
    >>> is_perfect_cube(8)
    False
    >>> is_perfect_cube(9)
    False
    >>> is_perfect_cube(10)
    False
    """
    if n < 2:
        return False
    for i in range(1, n + 1):
        if i * i * i == n:
            return True
    return False


def is_perfect_power(n: int) -> bool:
    """ Return True if n is perfect power, otherwise return False
    >>> is_perfect_power(1)
    False
    >>> is_perfect_power(2)
    True
    >>> is_perfect_power(3)
    True
    >>> is_perfect_power(4)
    True
    >>> is_perfect_power(5)
    False
    >>> is_perfect_power(6)
    False
    >>> is_perfect_power(7)
    False
    >>> is_perfect_power(8)
    False
    >>> is_perfect_