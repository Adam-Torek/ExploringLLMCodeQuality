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
        return fib(n - 1) + fib(n - 2)


def fib_recursive(n: int):
    """Return n-th Fibonacci number.
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
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memo(n: int):
    """Return n-th Fibonacci number.
    >>> fib_memo(10)
    55
    >>> fib_memo(1)
    1
    >>> fib_memo(8)
    21
    """
    memo = [0] * (n + 1)
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


def fib_iter(n: int):
    """Return n-th Fibonacci number.
    >>> fib_iter(10)
    55
    >>> fib_iter(1)
    1
    >>> fib_iter(8)
    21
    """
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


def fib_iter_memo(n: int):
    """Return n-th Fibonacci number.
    >>> fib_iter_memo(10)
    55
    >>> fib_iter_memo(1)
    1
    >>> fib_iter_memo(8)
    21
    """
    memo = [0] * (n + 1)
    memo[1] = 1
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, a + b
        memo[i] = b
    return memo[n]


def fib_iter_memo_2(n: int):
    """Return n-th Fibonacci number.
    >>> fib_iter_memo_2(10)
    55
    >>> fib_iter_memo_2(1)
    1
    >>> fib_iter_memo_2(8)
    21
    """
    memo = [0] * (n + 1)
    memo[1] = 1
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, a + b
        memo[i] = b
    return memo[n]


def fib_iter_memo_3(n: int):
    """Return n-th Fibonacci number.
    >>> fib_iter_memo_3(10)
    55
    >>> fib_iter_memo_3(1)
    1
    >>> fib_iter_memo_3(8)
    21
    """
    memo = [0] * (n + 1)
    memo[1] = 1
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, a + b
        memo[i] = b
    return memo[n]


def fib_iter_memo_4(n: int):
    """Return n-th Fibonacci number.
    >>> fib_iter_memo_4(10)
    55
    >>> fib_iter_