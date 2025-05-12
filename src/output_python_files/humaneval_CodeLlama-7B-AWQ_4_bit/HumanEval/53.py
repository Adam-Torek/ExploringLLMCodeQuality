def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y


def subtract(x: int, y: int):
    """Subtract two numbers x and y
    >>> subtract(2, 3)
    -1
    >>> subtract(5, 7)
    -2
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
    """Divide two numbers x and y
    >>> divide(2, 3)
    0.6666666666666666
    >>> divide(5, 7)
    0.71428571428571428
    """
    return x / y


def power(x: int, y: int):
    """Raise x to the power of y
    >>> power(2, 3)
    8
    >>> power(5, 7)
    16807
    """
    return x ** y


def square(x: int):
    """Return the square of x
    >>> square(2)
    4
    >>> square(5)
    25
    """
    return x ** 2


def cube(x: int):
    """Return the cube of x
    >>> cube(2)
    8
    >>> cube(5)
    125
    """
    return x ** 3


def factorial(x: int):
    """Return the factorial of x
    >>> factorial(2)
    2
    >>> factorial(5)
    120
    """
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


def is_prime(x: int):
    """Return True if x is a prime number, False otherwise
    >>> is_prime(2)
    True
    >>> is_prime(5)
    True
    >>> is_prime(10)
    False
    """
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def is_palindrome(x: int):
    """Return True if x is a palindrome, False otherwise
    >>> is_palindrome(2)
    False
    >>> is_palindrome(5)
    False
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(12345)
    False
    """
    return str(x) == str(x)[::-1]


def is_perfect_square(x: int):
    """Return True if x is a perfect square, False otherwise
    >>> is_perfect_square(2)
    False
    >>> is_perfect_square(5)
    False
    >>> is_perfect_square(12321)
    False
    >>> is_perfect_square(12345)
    False
    >>> is_perfect_square(123456)
    True
    """
    return x ** 0.5 == int(x ** 0.5)


def is_perfect_cube(x: int):
    """Return True if x is