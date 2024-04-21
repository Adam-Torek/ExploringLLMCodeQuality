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
    0
    >>> divide(5, 7)
    0
    """
    return x / y


def mod(x: int, y: int):
    """Modulo two numbers x and y
    >>> mod(2, 3)
    2
    >>> mod(5, 7)
    5
    """
    return x % y


def power(x: int, y: int):
    """Power two numbers x and y
    >>> power(2, 3)
    8
    >>> power(5, 7)
    125
    """
    return x ** y


def square(x: int):
    """Square a number x
    >>> square(2)
    4
    >>> square(5)
    25
    """
    return x ** 2


def cube(x: int):
    """Cube a number x
    >>> cube(2)
    8
    >>> cube(5)
    125
    """
    return x ** 3


def sqrt(x: int):
    """Square root of a number x
    >>> sqrt(2)
    1
    >>> sqrt(5)
    2
    """
    return x ** 0.5


def factorial(x: int):
    """Factorial of a number x
    >>> factorial(2)
    2
    >>> factorial(5)
    120
    """
    return x * factorial(x - 1) if x > 1 else 1


def fibonacci(x: int):
    """Fibonacci number x
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    """
    return fibonacci(x - 1) + fibonacci(x - 2) if x > 1 else x


def gcd(x: int, y: int):
    """Greatest common divisor of two numbers x and y
    >>> gcd(2, 3)
    1
    >>> gcd(5, 7)
    1
    """
    return gcd(y, x % y) if x % y != 0 else x


def lcm(x: int, y: int):
    """Least common multiple of two numbers x and y
    >>> lcm(2, 3)
    6
    >>> lcm(5, 7)
    35
    """
    return x * y // gcd(x, y)


def is_prime(x: int):
    """Check if a number x is prime
    >>> is_prime(2)
    True
    >>> is_prime(5)
    True
    >>> is_prime(10)
    False
    """
    return x > 1 and all(x % i for i in range(2, x))


def is_perfect(x: int):
    """Check if a number x is perfect
    >>> is_perfect(6)
    True
    >>> is_perfect(28)
    True
    >>> is_perfect(10)
    False
    """
    return x > 1 and sum(range(1, x)) == x


def is_abundant(x: int):
    """Check if a number x is abundant
    >>> is_abundant(12)