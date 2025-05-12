def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

def subtract(x: int, y: int) -> int:
    """Subtract y from x
    >>> subtract(7, 3)
    4
    >>> subtract(10, 5)
    5
    """
    return x - y

def multiply(x: int, y: int) -> int:
    """Multiply two numbers x and y
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35
    """
    return x * y

def divide(x: int, y: int) -> float:
    """Divide x by y
    >>> divide(7, 3)
    2.3333333333333333335
    >>> divide(10, 2)
    5.0
    """
    return x / y

def power(x: int, y: int) -> int:
    """Raise x to the power of y
    >>> power(2, 3)
    8
    >>> power(5, 2)
    25
    """
    return x ** y

def is_even(n: int) -> bool:
    """Check if a number is even
    >>> is_even(4)
    True
    >>> is_even(5)
    False
    """
    return n % 2 == 0

def is_prime(n: int) -> bool:
    """Check if a number is prime
    >>> is_prime(7)
    True
    >>> is_prime(12)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def factorial(n: int) -> int:
    """Calculate the factorial of a number
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number
    >>> fibonacci(7)
    13
    >>> fibonacci(10)
    55
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def sum_of_digits(n: int) -> int:
    """Calculate the sum of digits of a number
    >>> sum_of_digits(12345)
    15
    >>> sum_of_digits(9876)
    28
    """
    return sum(int(digit) for digit in str(n))

def reverse_string(s: str) -> str:
    """Reverse a string
    >>> reverse_string("hello")
    "olleh"
    >>> reverse_string("python")
    "nohtyp"
    """
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    """
    return s == reverse_string(s)

def count_vowels(s: str) -> int:
    """Count the number of vowels in a string
    >>> count_vowels("hello")
    1
    >>> count_vowels("python")
    1
    """
    vowels = "aeiou"
    return sum(s.count(v) for v in vowels)

def count_consonants(s: str) -> int:
    """Count the number of consonants in a string
    >>> count_consonants("hello")
    3
    >>> count_consonants("python")
    4