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
        return fib(n)


def fib(n: int):
    """
    fib returns n-th number that is a Fibonacci number.
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(7)
    13
    >>> fib(8)
    21
    >>> fib(9)
    34
    >>> fib(10)
    55
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_last_digit(n: int):
    """
    fib_last_digit returns the last digit of the n-th Fibonacci number.
    >>> fib_last_digit(1)
    1
    >>> fib_last_digit(2)
    1
    >>> fib_last_digit(3)
    2
    >>> fib_last_digit(4)
    3
    >>> fib_last_digit(5)
    5
    >>> fib_last_digit(6)
    8
    >>> fib_last_digit(7)
    1
    >>> fib_last_digit(8)
    4
    >>> fib_last_digit(9)
    2
    >>> fib_last_digit(10)
    5
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_last_digit(n - 1) + fib_last_digit(n - 2)


def fib_last_digit_naive(n: int):
    """
    fib_last_digit_naive returns the last digit of the n-th Fibonacci number.
    >>> fib_last_digit_naive(1)
    1
    >>> fib_last_digit_naive(2)
    1
    >>> fib_last_digit_naive(3)
    2
    >>> fib_last_digit_naive(4)
    3
    >>> fib_last_digit_naive(5)
    5
    >>> fib_last_digit_naive(6)
    8
    >>> fib_last_digit_naive(7)
    1
    >>> fib_last_digit_naive(8)
    4
    >>> fib_last_digit_naive(9)
    2
    >>> fib_last_digit_naive(10)
    5
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_last_digit_naive(n - 1) + fib_last_digit_naive(n - 2)


def fib_last_digit_recursive(n: int):
    """
    fib_last_digit_recursive returns the last digit of the n-th Fibonacci number.
    >>> fib_last_digit_recursive(1)
    1
    >>> fib_last_digit_recursive(2)
    1
    >>> fib_last_digit_recursive(3)
    2
    >>> fib_last_digit_recursive(4)
    3
    >>> fib_last_digit_recursive(5)
    5
    >>> fib_last_digit_recursive(6)
    8
    >>> fib_last_digit_recursive(7)
    1
    >>> fib