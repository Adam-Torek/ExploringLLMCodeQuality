def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        raise ValueError("n must be greater than 1")
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n


def largest_prime_factor_iterative(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor_iterative(13195)
    29
    >>> largest_prime_factor_iterative(2048)
    2
    """
    if n < 2:
        raise ValueError("n must be greater than 1")
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n


def largest_prime_factor_recursive(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor_recursive(13195)
    29
    >>> largest_prime_factor_recursive(2048)
    2
    """
    if n < 2:
        raise ValueError("n must be greater than 1")
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    while i * i <= n:
        if n % i == 0:
            return largest_prime_factor_recursive(n // i)
        i += 2
    return n


def largest_prime_factor_recursive_iterative(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor_recursive_iterative(13195)
    29
    >>> largest_prime_factor_recursive_iterative(2048)
    2
    """
    if n < 2:
        raise ValueError("n must be greater than 1")
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    while i * i <= n:
        if n % i == 0:
            return largest_prime_factor_recursive_iterative(n // i)
        i += 2
    return n


def largest_prime_factor_recursive_iterative_optimized(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor_recursive_iterative_optimized(13195)
    29
    >>> largest_prime_factor_recursive_iterative_optimized(2048)
    2
    """
    if n < 2:
        raise ValueError("n must be greater than 1")
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    while i * i <= n:
        if n % i == 0:
            return largest_prime_factor_recursive_iterative_optimized(n // i)
        i += 2
    return n


def largest_prime_factor_recursive_iterative_optimized_with_cache(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor_recursive_iterative_optimized