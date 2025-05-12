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
    a, b = 0, 1
    while True:
        c = a + b
        if isprime(c):
            return c
        a, b = b, c


def isprime(n: int):
    """
    isprime returns True if n is a prime number, False otherwise.
    >>> isprime(2)
    True
    >>> isprime(3)
    True
    >>> isprime(4)
    False
    >>> isprime(5)
    True
    >>> isprime(6)
    False
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()