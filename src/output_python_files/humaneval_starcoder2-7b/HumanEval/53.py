def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """

def subtract(x: int, y: int):
    """Subtract two numbers x and y
    >>> subtract(2, 3)
    -1
    >>> subtract(5, 7)
    -2
    """

def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35
    """

def divide(x: int, y: int):
    """Divide two numbers x and y
    >>> divide(2, 3)
    0
    >>> divide(5, 7)
    0
    """

def square(x: int):
    """Square a number x
    >>> square(2)
    4
    >>> square(5)
    25
    """

def cube(x: int):
    """Cube a number x
    >>> cube(2)
    8
    >>> cube(5)
    125
    """

def power(x: int, y: int):
    """Raise x to the power of y
    >>> power(2, 3)
    8
    >>> power(5, 7)
    78125
    """

def mod(x: int, y: int):
    """Return the remainder of x divided by y
    >>> mod(2, 3)
    2
    >>> mod(5, 7)
    5
    """

def get_biggest_number(*args: int):
    """Return the biggest number from a list of numbers
    >>> get_biggest_number(2, 3)
    3
    >>> get_biggest_number(5, 7)
    7
    """

def get_smallest_number(*args: int):
    """Return the smallest number from a list of numbers
    >>> get_smallest_number(2, 3)
    2
    >>> get_smallest_number(5, 7)
    5
    """

def count_positive_numbers(*args: int):
    """Return the number of positive numbers in a list of numbers
    >>> count_positive_numbers(2, 3)
    1
    >>> count_positive_numbers(5, 7)
    2
    """

def sum_positive_numbers(*args: int):
    """Return the sum of positive numbers in a list of numbers
    >>> sum_positive_numbers(2, 3)
    5
    >>> sum_positive_numbers(5, 7)
    12
    """

def get_even_numbers(start: int, end: int):
    """Return a list of even numbers between start and end
    >>> get_even_numbers(2, 3)
    [2]
    >>> get_even_numbers(5, 7)
    [6]
    """

def get_odd_numbers(start: int, end: int):
    """Return a list of odd numbers between start and end
    >>> get_odd_numbers(2, 3)
    [3]
    >>> get_odd_numbers(5, 7)
    [5, 7]
    """

def get_squares(start: int, end: int):
    """Return a list of squares between start and end
    >>> get_squares(2, 3)
    [4]
    >>> get_squares(5, 7)
    [25, 49]
    """

def get_cubes(start: int, end: int):
    """Return a list of cubes between start and end
    >>> get_cubes(2, 3)
    [8]
    >>> get_cubes(5, 7)
    [125, 343]
    """

def get_powers(start: int, end: int, power: int):
    """Return a list of numbers raised to the power between start and end
    >>> get_powers(2, 3, 2)
    [4]
    >>> get_powers(5, 7, 2)
    [25, 49]
    """

def get_mod(start: int, end: int, mod: int):
    """Return a list of numbers that are the remainder of start divided by mod between start and end
    >>> get_mod(2, 3, 2)
    [0]
    >>> get_mod(5, 7, 2)
    [1]
    """

def get_fibonacci_sequence(length: int):
    """Return