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
    if n <= 1:
        return 2
    fib_list = [2, 3]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
        if is_prime(fib_list[i]):
            return fib_list[i]
    return None

def is_prime(n: int):
    """
    is_prime returns True if n is prime and False otherwise.
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
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True