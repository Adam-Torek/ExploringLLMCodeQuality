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
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Return a list of the prime factors of a given number.
    >>> prime_factors(10)
    [2, 5]
    >>> prime_factors(15)
    [3, 3, 5]
    >>> prime_factors(7)
    [7]
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(101)
    [101]
    """
    factors = []
    divisor = 2
    while n > 1:
        if is_prime(divisor):
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
        else:
            divisor += 1
    return factors

def prime_factorization(n):
    """Return the prime factorization of a given number.
    >>> prime_factorization(10)
    [2, 5]
    >>> prime_factorization(15)
    [3, 5]
    >>> prime_factorization(101)
    [101]
    >>> prime_factorization(100)
    [2, 2, 5, 5]
    """
    factors = prime_factors(n)
    if len(factors) == 0:
        return [n]
    else:
        return factors

def is_perfect(n):
    """Return true if a given number is perfect, and false otherwise.
    >>> is_perfect(6)
    True
    >>> is_perfect(10)
    False
    >>> is_perfect(28)
    True
    >>> is_perfect(496)
    True
    """
    factors = prime_factorization(n)
    return n == sum(factors)

def is_abundant(n):
    """Return true if a given number is abundant, and false otherwise.
    >>> is_abundant(12)
    True
    >>> is_abundant(15)
    False
    >>> is_abundant(24)
    True
    >>> is_abundant(30)
    True
    """
    factors = prime_factorization(n)
    return sum(factors) > n

def is_deficient(n):
    """Return true if a given number is deficient, and false otherwise.
    >>> is_deficient(12)
    False
    >>> is_deficient(15)
    True
    >>> is_deficient(24)
    False
    >>> is_deficient(30)
    True
    """
    factors = prime_factorization(n)
    return sum(factors) < n

def is_deficient_or_abundant(n):
    """Return true if a given number is deficient or abundant, and false otherwise.
    >>> is_deficient_or_abundant(12)
    True
    >>> is_deficient_or_abundant(15)
    True
    >>> is_deficient_or_abundant(24)
    False
    >>> is_deficient_or_abundant(30)
    True
    """
    return is_deficient(n) or is_abundant(n)

def is_deficient_or_perfect(n):
    """Return true if a given number