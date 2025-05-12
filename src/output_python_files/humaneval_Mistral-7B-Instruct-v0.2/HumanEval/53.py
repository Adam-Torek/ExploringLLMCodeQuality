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
    >>> subtract(5, 3)
    2
    >>> subtract(10, 7)
    3
    """
    return x - y

def multiply(x: int, y: int):
    """Multiply x and y
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35
    """
    return x * y

def divide(x: int, y: int):
    """Divide x by y
    >>> divide(10, 2)
    5
    >>> divide(5, 2)
    2.5
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x: int, y: int):
    """Raise x to the power of y
    >>> power(2, 3)
    8
    >>> power(5, 2)
    25
    """
    return x ** y

def sqrt(x: int):
    """Calculate the square root of x
    >>> sqrt(16)
    4
    >>> sqrt(25)
    5
    """
    import math
    return int(math.sqrt(x))

def factorial(x: int):
    """Calculate the factorial of x
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if x == 0:
        return 1
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

def fibonacci(n: int):
    """Calculate the nth Fibonacci number
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
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b

def gcd(x: int, y: int):
    """Calculate the greatest common divisor of x and y
    >>> gcd(2, 5)
    1
    >>> gcd(3, 5)
    1
    >>> gcd(3, 6)
    3
    >>> gcd(10, 15)
    5
    >>> gcd(12, 18)
    6
    """
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x: int, y: int):
    """Calculate the least common multiple of x and y
    >>> lcm(2, 5)
    10
    >>> lcm(3, 5)
    1