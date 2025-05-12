def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

def is_even(number: int) -> bool:
    """ Given a positive integer, return True if it is even, False otherwise.
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    """

def is_odd(number: int) -> bool:
    """ Given a positive integer, return True if it is odd, False otherwise.
    >>> is_odd(2)
    False
    >>> is_odd(3)
    True
    """

def is_prime(number: int) -> bool:
    """ Given a positive integer, return True if it is prime, False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    """

def is_perfect(number: int) -> bool:
    """ Given a positive integer, return True if it is perfect, False otherwise.
    >>> is_perfect(6)
    True
    >>> is_perfect(7)
    False
    """

def is_abundant(number: int) -> bool:
    """ Given a positive integer, return True if it is abundant, False otherwise.
    >>> is_abundant(6)
    False
    >>> is_abundant(12)
    True
    """

def is_deficient(number: int) -> bool:
    """ Given a positive integer, return True if it is deficient, False otherwise.
    >>> is_deficient(6)
    True
    >>> is_deficient(12)
    False
    """

def is_perfect_square(number: int) -> bool:
    """ Given a positive integer, return True if it is a perfect square, False otherwise.
    >>> is_perfect_square(6)
    False
    >>> is_perfect_square(9)
    True
    """

def is_palindrome(number: int) -> bool:
    """ Given a positive integer, return True if it is a palindrome, False otherwise.
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(12345)
    False
    """

def is_armstrong(number: int) -> bool:
    """ Given a positive integer, return True if it is an Armstrong number, False otherwise.
    >>> is_armstrong(153)
    True
    >>> is_armstrong(154)
    False
    """

def is_happy(number: int) -> bool:
    """ Given a positive integer, return True if it is a happy number, False otherwise.
    >>> is_happy(153)
    True
    >>> is_happy(154)
    False
    """

def is_lucky(number: int) -> bool:
    """ Given a positive integer, return True if it is a lucky number, False otherwise.
    >>> is_lucky(153)
    True
    >>> is_lucky(154)
    False
    """

def is_happy_lucky(number: int) -> bool:
    """ Given a positive integer, return True if it is a happy or lucky number, False otherwise.
    >>> is_happy_lucky(153)
    True
    >>> is_happy_lucky(154)
    False
    """

def is_happy_lucky_armstrong(number: int) -> bool:
    """ Given a positive integer, return True if it is a happy, lucky or Armstrong number, False otherwise.
    >>> is_happy_lucky_armstrong(153)
    True
    >>> is_happy_lucky_armstrong(154)
    False
    """

def is_happy_lucky_armstrong_perfect(number: int) -> bool:
    """ Given a positive integer, return True if it is a happy, lucky, Armstrong or perfect number, False otherwise.
    >>> is_happy_lucky_armstrong_perfect(153)
    True
    >>> is_happy_lucky_armstrong_perfect(154)
    False
    """

def is_