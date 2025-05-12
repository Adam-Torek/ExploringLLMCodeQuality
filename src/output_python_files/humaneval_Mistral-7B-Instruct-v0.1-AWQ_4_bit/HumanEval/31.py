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
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_factorization(n):
    """Return a list of the prime factors of n.
    >>> prime_factorization(12)
    [2, 2, 3]
    >>> prime_factorization(101)
    [101]
    >>> prime_factorization(11)
    [11]
    >>> prime_factorization(13441)
    [13441]
    >>> prime_factorization(61)
    [61]
    >>> prime_factorization(4)
    [2, 2]
    >>> prime_factorization(1)
    []
    """
    if n == 1:
        return []
    if n == 2:
        return [2]
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


def prime_factorization_iterative(n):
    """Return a list of the prime factors of n.
    >>> prime_factorization_iterative(12)
    [2, 2, 3]
    >>> prime_factorization_iterative(101)
    [101]
    >>> prime_factorization_iterative(11)
    [11]
    >>> prime_factorization_iterative(13441)
    [13441]
    >>> prime_factorization_iterative(61)
    [61]
    >>> prime_factorization_iterative(4)
    [2, 2]
    >>> prime_factorization_iterative(1)
    []
    """
    if n == 1:
        return []
    if n == 2:
        return [2]
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


def prime_factorization_recursive(n):
    """Return a list of the prime factors of n.
    >>> prime_factorization_recursive(12)
    [2, 2, 3]
    >>> prime_factorization_recursive(101)
    [101]
    >>> prime_factorization_recursive(11)
    [11]
    >>> prime_factorization_recursive(13441)
    [13441]
    >>> prime_factorization_recursive(61)
    [61]
    >>> prime_factorization_recursive(4)
    [2, 2]
    >>> prime_factorization_recursive(1)
    []
    """
    if n == 1:
        return []
    if n == 2:
        return [2]
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1: