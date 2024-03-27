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


def factorial(x: int):
    """Factorial of a number
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
    """Fibonacci number
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(x: int, y: int):
    """Greatest common divisor of two numbers x and y
    >>> gcd(2, 3)
    1
    >>> gcd(5, 7)
    1
    """
    if x == 0:
        return y
    elif y == 0:
        return x
    elif x > y:
        return gcd(x - y, y)
    else:
        return gcd(x, y - x)


def lcm(x: int, y: int):
    """Least common multiple of two numbers x and y
    >>> lcm(2, 3)
    6
    >>> lcm(5, 7)
    35
    """
    return x * y / gcd(x, y)


def is_prime(x: int):
    """Check if a number is prime
    >>> is_prime(2)
    True
    >>> is_prime(5)
    True
    >>> is_prime(10)
    False
    """
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


def is_perfect(x: int):
    """Check if a number is perfect
    >>> is_perfect(6)
    True
    >>> is_perfect(28)
    True
    >>> is_perfect(10)
    False
    """
    return x == sum(range(1, x))


def is_abundant(x: int):
    """Check if a number is abundant
    >>> is_abundant(12)
    True
    >>> is_abundant(28)
    False
    >>> is_abundant(10)
    False
    """
    return x > sum(range(1, x))


def is_deficient(x