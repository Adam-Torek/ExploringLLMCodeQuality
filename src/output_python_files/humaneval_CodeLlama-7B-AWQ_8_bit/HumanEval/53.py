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
    119026
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


def fibonacci(n: int):
    """Return the nth Fibonacci number
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(7)
    13
    >>> fibonacci(8)
    21
    >>> fibonacci(9)
    34
    >>> fibonacci(10)
    55
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(x: int, y: int):
    """Return the greatest common divisor of x and y
    >>> gcd(2, 3)
    1
    >>> gcd(5, 7)
    1
    >>> gcd(10, 15)
    5
    >>> gcd(100, 150)
    50
    """
    if x == 0:
        return y
    elif y == 0:
        return x
    elif x > y:
        return gcd(y, x % y)
    else:
        return gcd(y, x)


def lcm(x: int, y: int):
    """Return the least common multiple of x and y
    >>> lcm(2, 3)
    6
    >>> lcm(5, 7)
    35
    >>> lcm(10, 15)
    30
    >>> lcm(100, 150)
    150
    """
    return x * y // gcd(x, y)


def is_prime(x: int):
    """Return True if x is a prime number, otherwise return False