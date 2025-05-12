def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

def least_common_multiple(a: int, b: int) -> int:
    """ Return a least common multiple of two integers a and b
    >>> least_common_multiple(3, 5)
    15
    >>> least_common_multiple(25, 15)
    75
    """

def is_prime(n: int) -> bool:
    """ Return True if n is prime, False otherwise
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(13)
    True
    """

def is_perfect(n: int) -> bool:
    """ Return True if n is perfect, False otherwise
    >>> is_perfect(6)
    True
    >>> is_perfect(10)
    False
    """

def is_deficient(n: int) -> bool:
    """ Return True if n is deficient, False otherwise
    >>> is_deficient(6)
    False
    >>> is_deficient(10)
    True
    """

def is_abundant(n: int) -> bool:
    """ Return True if n is abundant, False otherwise
    >>> is_abundant(6)
    True
    >>> is_abundant(10)
    False
    """

def is_perfect_square(n: int) -> bool:
    """ Return True if n is a perfect square, False otherwise
    >>> is_perfect_square(6)
    False
    >>> is_perfect_square(10)
    False
    >>> is_perfect_square(16)
    True
    """

def is_palindrome(n: int) -> bool:
    """ Return True if n is a palindrome, False otherwise
    >>> is_palindrome(1)
    True
    >>> is_palindrome(10)
    False
    >>> is_palindrome(121)
    True
    """

def is_armstrong(n: int) -> bool:
    """ Return True if n is an Armstrong number, False otherwise
    >>> is_armstrong(1)
    True
    >>> is_armstrong(10)
    False
    >>> is_armstrong(153)
    True
    """

def is_strong(n: int) -> bool:
    """ Return True if n is a strong number, False otherwise
    >>> is_strong(1)
    True
    >>> is_strong(10)
    False
    >>> is_strong(145)
    True
    """

def is_deficient_perfect_abundant(n: int) -> bool:
    """ Return True if n is deficient, perfect or abundant, False otherwise
    >>> is_deficient_perfect_abundant(6)
    True
    >>> is_deficient_perfect_abundant(10)
    False
    >>> is_deficient_perfect_abundant(12)
    False
    """

def is_deficient_perfect_abundant_strong(n: int) -> bool:
    """ Return True if n is deficient, perfect, abundant or strong, False otherwise
    >>> is_deficient_perfect_abundant_strong(6)
    True
    >>> is_deficient_perfect_abundant_strong(10)
    False
    >>> is_deficient_perfect_abundant_strong(12)
    False
    """

def is_deficient_perfect_abundant_strong_palindrome(n: int) -> bool:
    """ Return True if n is deficient, perfect, abundant, strong or palindrome, False otherwise
    >>> is_deficient_perfect_abundant_strong_palindrome(6)
    True
    >>> is_deficient_perfect_abundant_strong_palindrome(10)
    False
    >>> is_deficient_perfect_abundant_strong_palindrome(12)
    False
    """

def is_deficient_perfect_abundant_strong_palindrome_armstrong(n: int) -> bool:
    """ Return True if n is deficient, perfect, abundant, strong, palindrome or armstrong, False otherwise
    >>> is_deficient_perfect_abundant_strong_palindrome_armstrong(6)
    True
    >>> is_