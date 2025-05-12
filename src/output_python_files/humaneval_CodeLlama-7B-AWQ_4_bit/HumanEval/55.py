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


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    assert fib(10) == 55


def run_fib():
    """Run the test for fib."""
    test_fib()


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


def test_fib_iter():
    assert fib_iter(1) == 1
    assert fib_iter(2) == 1
    assert fib_iter(7) == 13
    assert fib_iter(10) == 55


def run_fib_iter():
    """Run the test for fib_iter."""
    test_fib_iter()


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


def test_fib_rec():
    assert fib_rec(1) == 1
    assert fib_rec(2) == 1
    assert fib_rec(7) == 13
    assert fib_rec(10) == 55


def run_fib_rec():
    """Run the test for fib_rec."""
    test_fib_rec()


def fib_rec_memo(n: int, memo: dict = None):
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
        result = n
    else:
        result = fib_rec_memo(n - 1, memo) + fib_rec_memo(n - 2, memo)
    memo[n] = result
    return result


def test_fib_rec_memo():
    assert fib_rec_memo(1) == 1
    assert fib_rec_memo(2) == 1
    assert fib_rec_memo(7) == 13
    assert fib_rec_memo(10) == 55


def run_fib_rec_memo():
    """Run the test for fib_rec_memo."""
    test_fib_rec_memo()


def fib_rec_memo_2(n: int, memo: dict = None):
    """Return n-th Fibonacci number.