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

if __name__ == "__main__":
    import doctest
    doctest.testmod()