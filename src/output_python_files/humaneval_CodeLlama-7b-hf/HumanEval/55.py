def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


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


def fib_rec(n: int):
    """Return n-th Fibonacci number.
    >>> fib_rec(10)
    55
    >>> fib_rec(1)
    1
    >>> fib_rec(8)
    21
    """
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_rec_memo(n: int, memo: list = None):
    """Return n-th Fibonacci number.
    >>> fib_rec_memo(10)
    55
    >>> fib_rec_memo(1)
    1
    >>> fib_rec_memo(8)
    21
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    else:
        memo[n] = fib_rec_memo(n - 1, memo) + fib_rec_memo(n - 2, memo)
        return memo[n]


def fib_rec_tab(n: int):
    """Return n-th Fibonacci number.
    >>> fib_rec_tab(10)
    55
    >>> fib_rec_tab(1)
    1
    >>> fib_rec_tab(8)
    21
    """
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


def fib_rec_tab_memo(n: int):
    """Return n-th Fibonacci number.
    >>> fib_rec_tab_memo(10)
    55
    >>> fib_rec_tab_memo(1)
    1
    >>> fib_rec_tab_memo(8)
    21
    """
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


def fib_rec_tab_memo_2(n: int):
    """Return n-th Fibonacci number.
    >>> fib_rec_tab_memo_2(10)
    55
    >>> fib_rec_tab_memo_2(1)
    1
    >>> fib_rec_tab_memo_2(8)
    21
    """
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


def fib_rec_tab_memo_3(n: int):
    """Return n-th Fibonacci number.
    >>> fib_rec