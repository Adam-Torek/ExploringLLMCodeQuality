def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

def subtract(x: int, y: int):
    """Subtract y from x
    >>> subtract(7, 3)
    4
    >>> subtract(10, 5)
    5
    """
    return x - y

def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35
    """
    return x * y

def divide(x: int, y: int):
    """Divide x by y
    >>> divide(10, 2)
    5.0
    >>> divide(15, 3)
    5.0
    """
    return x / y

def power(x: int, y: int):
    """Raise x to the power of y
    >>> power(2, 3)
    8
    >>> power(5, 2)
    25
    """
    return x ** y

def modulo(x: int, y: int):
    """Find the remainder of x divided by y
    >>> modulo(10, 3)
    1
    >>> modulo(15, 4)
    3
    """
    return x % y

def factorial(n: int):
    """Find the factorial of n
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n: int):
    """Check if a number is prime
    >>> is_prime(7)
    True
    >>> is_prime(12)
    False
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def fibonacci(n: int):
    """Find the nth Fibonacci number
    >>> fibonacci(7)
    13
    >>> fibonacci(10)
    55
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def sum_of_digits(n: int):
    """Find the sum of digits of a number
    >>> sum_of_digits(12345)
    15
    >>> sum_of_digits(6789)
    24
    """
    return sum(int(digit) for digit in str(n))

def reverse_string(s: str):
    """Reverse a string
    >>> reverse_string("hello")
    "olleh"
    >>> reverse_string("world")
    "dlrow"
    """
    return s[::-1]

def is_palindrome(s: str):
    """Check if a string is a palindrome
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    """
    return s == s[::-1]

def count_vowels(s: str):
    """Count the number of vowels in a string
    >>> count_vowels("hello")
    2
    >>> count_vowels("python")
    2
    """
    vowels