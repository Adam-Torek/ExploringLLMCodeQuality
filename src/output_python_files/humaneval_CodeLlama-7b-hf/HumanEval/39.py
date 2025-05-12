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


def is_prime(n: int):
    """
    is_prime returns True if n is prime, False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    """
    if n == 2:
        return True
    elif n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


def is_fib(n: int):
    """
    is_fib returns True if n is a Fibonacci number, False otherwise.
    >>> is_fib(2)
    True
    >>> is_fib(3)
    True
    >>> is_fib(4)
    False
    >>> is_fib(5)
    True
    >>> is_fib(6)
    False
    >>> is_fib(7)
    True
    >>> is_fib(8)
    False
    >>> is_fib(9)
    False
    >>> is_fib(10)
    False
    """
    if n == 2:
        return True
    elif n == 3:
        return True
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


def is_fib_prime(n: int):
    """
    is_fib_prime returns True if n is a Fibonacci number and it's also prime,
    False otherwise.
    >>> is_fib_prime(2)
    True
    >>> is_fib_prime(3)
    True
    >>> is_fib_prime(4)
    False
    >>> is_fib_prime(5)
    True
    >>> is_fib_prime(6)
    False
    >>> is_fib_prime(7)
    True
    >>> is_fib_prime(8)
    False
    >>> is_fib_prime(9)
    False
    >>> is_fib_prime(10)
    False
    """
    if n == 2:
        return True
    elif n == 3:
        return True
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


def is_fib_prime_fast(n: int):
    """
    is_fib_prime_fast returns True if n is a Fibonacci number and it's also
    prime, False otherwise.
    >>> is_fib_prime_fast(2)
    True