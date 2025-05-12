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
    0.6666666666666667
    >>> divide(5, 7)
    0.7142857142857143
    """
    return x / y

def modulo(x: int, y: int):
    """Modulo of two numbers x and y
    >>> modulo(2, 3)
    0
    >>> modulo(5, 7)
    2
    """
    return x % y

def factorial(n: int):
    """Factorial of a number n
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n: int):
    """Fibonacci sequence of a number n
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
        return fibonacci(n-1) + fibonacci(n-2)

def sum_of_squares(n: int):
    """Sum of squares of first n natural numbers
    >>> sum_of_squares(0)
    0
    >>> sum_of_squares(1)
    1
    >>> sum_of_squares(2)
    5
    >>> sum_of_squares(3)
    10
    >>> sum_of_squares(4)
    17
    >>> sum_of_squares(5)
    25
    >>> sum_of_squares(6)
    36
    >>> sum_of_squares(7)
    49
    >>> sum_of_squares(8)
    64
    >>> sum_of_squares(9)
    81
    >>> sum_of_squares(10)
    100
    """
    return sum([i**2 for i in range(1, n+1)])

def sum_of_cubes(n: int):
    """Sum of cubes of first n natural numbers
    >>> sum_of_cubes(0)
    0
    >>> sum_of_cubes(1)
    1
    >>> sum_of_cubes(2)
    8
    >>> sum_of_cubes(3)
    27
    >>> sum_of_cubes(4)
    64
    >>> sum_of