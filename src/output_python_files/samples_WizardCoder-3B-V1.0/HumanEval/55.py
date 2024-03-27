def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

def fib_recursive(n: int):
    """Return n-th Fibonacci number using recursion.
    >>> fib_recursive(10)
    55
    >>> fib_recursive(1)
    1
    >>> fib_recursive(8)
    21
    """
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n: int):
    """Return n-th Fibonacci number using iteration.
    >>> fib_iterative(10)
    55
    >>> fib_iterative(1)
    1
    >>> fib_iterative(8)
    21
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    import doctest
    doctest.testmod()<|endoftext|>