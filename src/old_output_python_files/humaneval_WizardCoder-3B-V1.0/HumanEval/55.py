def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

def fib_iterative(n: int):
    """Return n-th Fibonacci number using an iterative approach.
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

def fib_recursive(n: int):
    """Return n-th Fibonacci number using a recursive approach.
    >>> fib_recursive(10)
    55
    >>> fib_recursive(1)
    1
    >>> fib_recursive(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_memoized(n: int):
    """Return n-th Fibonacci number using a memoized approach.
    >>> fib_memoized(10)
    55
    >>> fib_memoized(1)
    1
    >>> fib_memoized(8)
    21
    """
    memo = {0: 0, 1: 1}
    def fib_helper(n: int):
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib_helper(n-1) + fib_helper(n-2)
            return memo[n]
    return fib_helper(n)

def main():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()<|endoftext|>