def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

def is_prime(n: int):
    """Return True if n is prime, False otherwise. Assume n > 1.
    >>> is_prime(13)
    True
    >>> is_prime(12)
    False
    """

def prime_factors(n: int):
    """Return a list of prime factors of n. Assume n > 1.
    >>> prime_factors(13195)
    [5, 7, 13, 29]
    >>> prime_factors(2048)
    [2, 2, 2, 2, 2, 2, 2, 2]
    """

def is_palindrome(n: int):
    """Return True if n is a palindrome, False otherwise.
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(12345)
    False
    """

def is_perfect(n: int):
    """Return True if n is a perfect number, False otherwise.
    >>> is_perfect(6)
    True
    >>> is_perfect(12)
    False
    """

def is_abundant(n: int):
    """Return True if n is an abundant number, False otherwise.
    >>> is_abundant(6)
    False
    >>> is_abundant(12)
    True
    """

def is_deficient(n: int):
    """Return True if n is a deficient number, False otherwise.
    >>> is_deficient(6)
    True
    >>> is_deficient(12)
    False
    """

def is_perfect_square(n: int):
    """Return True if n is a perfect square, False otherwise.
    >>> is_perfect_square(12)
    False
    >>> is_perfect_square(16)
    True
    """

def is_power_of_two(n: int):
    """Return True if n is a power of two, False otherwise.
    >>> is_power_of_two(12)
    False
    >>> is_power_of_two(16)
    True
    """

def is_power_of_three(n: int):
    """Return True if n is a power of three, False otherwise.
    >>> is_power_of_three(12)
    False
    >>> is_power_of_three(16)
    False
    >>> is_power_of_three(27)
    True
    """

def is_power_of_five(n: int):
    """Return True if n is a power of five, False otherwise.
    >>> is_power_of_five(12)
    False
    >>> is_power_of_five(16)
    False
    >>> is_power_of_five(25)
    True
    """

def is_power_of_seven(n: int):
    """Return True if n is a power of seven, False otherwise.
    >>> is_power_of_seven(12)
    False
    >>> is_power_of_seven(16)
    False
    >>> is_power_of_seven(49)
    True
    """

def is_power_of_n(n: int, m: int):
    """Return True if n is a power of m, False otherwise.
    >>> is_power_of_n(12, 2)
    False
    >>> is_power_of_n(16, 2)
    True
    >>> is_power_of_n(16, 3)
    False
    >>> is_power_of_n(27, 3)
    True
    """

def is_power_of_two_or_three(n: int):
    """Return True if n is a power of two or three, False otherwise.
    >>> is_power_of_two_or_three(12)
    False
    >>> is_power_of_two_or_three(16)
    True
    >>> is_power_of_two_or_three(