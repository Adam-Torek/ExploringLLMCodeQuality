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
    [2, 2, 5]
    >>> prime_factorization(15)
    [3, 5]
    >>> prime_factorization(7)
    [7]
    >>> prime_factorization(100)
    [2, 2, 5, 5]
    >>> prime_factorization(101)
    [101]
    """
    factors = []
    while n > 1:
        factors.extend(prime_factors(n))
        n = 1
        for factor in factors:
            n //= factor
    return factors

def is_permutation(a, b):
    """Return true if a is a permutation of b, and false otherwise.
    >>> is_permutation(1234, 4321)
    True
    >>> is_permutation(1234, 432)
    False
    >>> is_permutation(123, 432)
    False
    >>> is_permutation(123, 124)
    False
    """
    return sorted(str(a)) == sorted(str(b))

def is_palindrome(n):
    """Return true if a given number is a palindrome, and false otherwise.
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(12345)
    False
    >>> is_palindrome(1001)
    True
    """
    return str(n) == str(n)[::-1]

def is_prime_palindrome(n):
    """Return true if a given number is a prime palindrome, and false otherwise.
    >>> is_prime_palindrome(12321)
    True
    >>> is_prime_palindrome(12345)
    False
    >>> is_prime_palindrome(1001)
    False
    """
    return is_prime(n) and is_palindrome(n)

def is_prime_permutation_palindrome(n):
    """Return true if a given number is a prime permutation palindrome, and false otherwise.
    >>> is_prime_permutation_palindrome(12321)
    True
    >>> is_prime_permutation_palindrome(12345)
    False
    >>> is_prime_permutation_palindrome(1001)
    True