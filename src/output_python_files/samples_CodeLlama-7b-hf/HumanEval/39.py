def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return prime_fib(n - 1) + prime_fib(n - 2)


def prime_fib_list(n: int):
    """
    prime_fib_list returns a list of first n prime Fibonacci numbers.
    >>> prime_fib_list(1)
    [2]
    >>> prime_fib_list(2)
    [2, 3]
    >>> prime_fib_list(3)
    [2, 3, 5]
    >>> prime_fib_list(4)
    [2, 3, 5, 13]
    >>> prime_fib_list(5)
    [2, 3, 5, 13, 89]
    """
    if n == 1:
        return [2]
    elif n == 2:
        return [2, 3]
    else:
        return prime_fib_list(n - 1) + [prime_fib(n)]


def prime_fib_list_with_memo(n: int):
    """
    prime_fib_list_with_memo returns a list of first n prime Fibonacci numbers.
    >>> prime_fib_list_with_memo(1)
    [2]
    >>> prime_fib_list_with_memo(2)
    [2, 3]
    >>> prime_fib_list_with_memo(3)
    [2, 3, 5]
    >>> prime_fib_list_with_memo(4)
    [2, 3, 5, 13]
    >>> prime_fib_list_with_memo(5)
    [2, 3, 5, 13, 89]
    """
    if n == 1:
        return [2]
    elif n == 2:
        return [2, 3]
    else:
        return prime_fib_list_with_memo(n - 1) + [prime_fib_with_memo(n)]


def prime_fib_with_memo(n: int):
    """
    prime_fib_with_memo returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib_with_memo(1)
    2
    >>> prime_fib_with_memo(2)
    3
    >>> prime_fib_with_memo(3)
    5
    >>> prime_fib_with_memo(4)
    13
    >>> prime_fib_with_memo(5)
    89
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return prime_fib_with_memo(n - 1) + prime_fib_with_memo(n - 2)


def prime_fib_with_memo_list(n: int):
    """
    prime_fib_with_memo_list returns a list of first n prime Fibonacci numbers.
    >>> prime_fib_with_memo_list(1)
    [2]
    >>> prime_fib_with_memo_list(2)
    [2, 3]
    >>> prime_fib_with_memo_list(3)
    [2, 3, 5]
    >>> prime_fib_with_memo_list(4)
    [2, 3, 5, 13]
    >>> prime_fib