def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

def is_prime(number: int) -> bool:
    """ Given a positive integer, it checks if it is a prime number.

    Return True if the number is prime, False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(1)
    False
    """

def is_perfect(number: int) -> bool:
    """ Given a positive integer, it checks if it is a perfect number.

    Return True if the number is perfect, False otherwise.
    >>> is_perfect(6)
    True
    >>> is_perfect(1)
    False
    """

def is_amicable(number: int) -> bool:
    """ Given a positive integer, it checks if it is an amicable number.

    Return True if the number is amicable, False otherwise.
    >>> is_amicable(220)
    True
    >>> is_amicable(1)
    False
    """

def is_deficient(number: int) -> bool:
    """ Given a positive integer, it checks if it is a deficient number.

    Return True if the number is deficient, False otherwise.
    >>> is_deficient(220)
    False
    >>> is_deficient(1)
    False
    """

def is_abundant(number: int) -> bool:
    """ Given a positive integer, it checks if it is an abundant number.

    Return True if the number is abundant, False otherwise.
    >>> is_abundant(220)
    False
    >>> is_abundant(1)
    False
    """

def is_perfect_square(number: int) -> bool:
    """ Given a positive integer, it checks if it is a perfect square.

    Return True if the number is a perfect square, False otherwise.
    >>> is_perfect_square(220)
    False
    >>> is_perfect_square(1)
    False
    """

def is_palindrome(number: int) -> bool:
    """ Given a positive integer, it checks if it is a palindrome.

    Return True if the number is a palindrome, False otherwise.
    >>> is_palindrome(220)
    False
    >>> is_palindrome(1)
    False
    """

def is_fibonacci(number: int) -> bool:
    """ Given a positive integer, it checks if it is a Fibonacci number.

    Return True if the number is a Fibonacci number, False otherwise.
    >>> is_fibonacci(220)
    False
    >>> is_fibonacci(1)
    False
    """

def is_triangular(number: int) -> bool:
    """ Given a positive integer, it checks if it is a triangular number.

    Return True if the number is a triangular number, False otherwise.
    >>> is_triangular(220)
    False
    >>> is_triangular(1)
    False
    """

def is_square(number: int) -> bool:
    """ Given a positive integer, it checks if it is a square number.

    Return True if the number is a square number, False otherwise.
    >>> is_square(220)
    False
    >>> is_square(1)
    False
    """

def is_pentagonal(number: int) -> bool:
    """ Given a positive integer, it checks if it is a pentagonal number.

    Return True if the number is a pentagonal number, False otherwise.
    >>> is_pentagonal(220)
    False
    >>> is_pentagonal(1)
    False
    """

def is_hexagonal(number: int) -> bool:
    """ Given a positive integer, it checks if it is a hexagonal number.

    Return True if the number is a hexagonal number, False otherwise.
    >>> is_hexagonal(220)
    False
    >>> is_hexagonal(1)
    False
    """

def is_heptagonal(number: int) -> bool:
    """ Given a positive integer, it checks if it is a heptagonal number.

    Return True if the number is a heptagonal number, False otherwise.
    >>> is_heptagonal(220)
    False
    >>> is_heptagonal(1)