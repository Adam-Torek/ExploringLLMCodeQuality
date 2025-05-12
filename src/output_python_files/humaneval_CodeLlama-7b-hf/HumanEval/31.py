def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
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


def is_prime_fast(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime_fast(6)
    False
    >>> is_prime_fast(101)
    True
    >>> is_prime_fast(11)
    True
    >>> is_prime_fast(13441)
    True
    >>> is_prime_fast(61)
    True
    >>> is_prime_fast(4)
    False
    >>> is_prime_fast(1)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_fastest(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime_fastest(6)
    False
    >>> is_prime_fastest(101)
    True
    >>> is_prime_fastest(11)
    True
    >>> is_prime_fastest(13441)
    True
    >>> is_prime_fastest(61)
    True
    >>> is_prime_fastest(4)
    False
    >>> is_prime_fastest(1)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_fastest_2(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime_fastest_2(6)
    False
    >>> is_prime_fastest_2(101)
    True
    >>> is_prime_fastest_2(11)
    True
    >>> is_prime_fastest_2(13441)
    True
    >>> is_prime_fastest_2(61)
    True
    >>> is_prime_fastest_2(4)
    False
    >>> is_prime_fastest_2(1)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_fastest_3(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime_fastest_3(6)
    False
    >>> is_prime_fastest_3(101)
    True
    >>> is_prime_fastest_3(11)
    True
    >>> is_prime_fastest_3(13441)
    True
    >>> is_prime_fastest_3(61)
    True
    >>> is_prime_fastest_3(4)
    False
    >>> is_prime_fastest_3(1)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_fastest_4(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime_fastest_4(6)
    False
    >>> is_prime_fastest_4(101)
    True
    >>> is_prime_fastest_4(11)
    True