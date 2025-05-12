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
    prime_fib_list returns a list of first n Fibonacci numbers that are prime.
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
        return prime_fib_list(n - 1) + [prime_fib(n - 1)]


def prime_fib_list_sum(n: int):
    """
    prime_fib_list_sum returns the sum of first n Fibonacci numbers that are prime.
    >>> prime_fib_list_sum(1)
    2
    >>> prime_fib_list_sum(2)
    5
    >>> prime_fib_list_sum(3)
    13
    >>> prime_fib_list_sum(4)
    37
    >>> prime_fib_list_sum(5)
    159
    """
    if n == 1:
        return 2
    elif n == 2:
        return 5
    else:
        return prime_fib_list_sum(n - 1) + prime_fib(n - 1)


def prime_fib_list_sum_fast(n: int):
    """
    prime_fib_list_sum_fast returns the sum of first n Fibonacci numbers that are prime.
    >>> prime_fib_list_sum_fast(1)
    2
    >>> prime_fib_list_sum_fast(2)
    5
    >>> prime_fib_list_sum_fast(3)
    13
    >>> prime_fib_list_sum_fast(4)
    37
    >>> prime_fib_list_sum_fast(5)
    159
    """
    if n == 1:
        return 2
    elif n == 2:
        return 5
    else:
        return prime_fib_list_sum_fast(n - 1) + prime_fib_list_sum(n - 2)


def prime_fib_list_sum_fastest(n: int):
    """
    prime_fib_list_sum_fastest returns the sum of first n Fibonacci numbers that are prime.
    >>> prime_fib_list_sum_fastest(1)
    2
    >>> prime_fib_list_sum_fastest(2)
    5
    >>> prime_fib_list_sum_fastest(3)
    13
    >>> prime_fib_list_sum_fastest(4)
    37
    >>> prime_fib_list_sum_fastest(5)
    159
    """
    if n == 1:
        return 2
    elif n == 2:
        return 5
    else:
        return prime_fib_list_sum_fastest(n - 1) + prime_fib_list_sum_fast(n -