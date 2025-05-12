def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_memo(n: int):
    """Return n-th Fibonacci number using memoization.
    >>> fib_memo(10)
    55
    >>> fib_memo(1)
    1
    >>> fib_memo(8)
    21
    """
    memo = [1, 1]
    if len(memo) < n:
        memo.extend([fib(i) for i in range(2, n)])
    return memo[n-1]


def fib_iterative(n: int):
    """Return n-th Fibonacci number using an iterative approach.
    >>> fib_iterative(10)
    55
    >>> fib_iterative(1)
    1
    >>> fib_iterative(8)
    21
    """
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a + b
    return b


def fib_recursive(n: int):
    """Return n-th Fibonacci number using recursion.
    >>> fib_recursive(10)
    55
    >>> fib_recursive(1)
    1
    >>> fib_recursive(8)
    21
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_matrix(n: int):
    """Return n-th Fibonacci number using matrix exponentiation.
    >>> fib_matrix(10)
    55
    >>> fib_matrix(1)
    1
    >>> fib_matrix(8)
    21
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        matrix = [[1, 1], [1, 0]]
        for i in range(2, n):
            matrix = matrix * matrix
        return matrix[i-1][i-2]


def fib_generator(n: int):
    """Return an infinite generator that yields the n-th Fibonacci number.
    >>> fib_generator(10)
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    >>> fib_generator(1)
    1
    >>> fib_generator(8)
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    """
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def fib_coroutine(n: int):
    """Return a coroutine that yields the n-th Fibonacci number.
    >>> fib_coroutine(10)
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    >>> fib_coroutine(1)
    1
    >>> fib_coroutine(8)
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    """
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def fib_async(n: int):
    """Return an async function that yields the n-th Fibonacci number.
    >>> fib_async(10)
    1
    1
    2
    3
    5
    8
    13
    21