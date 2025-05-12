def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(n):
    """Return a list of all prime numbers up to and including n.
    >>> find_primes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> find_primes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> find_primes(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def find_primes_list_comprehension(n):
    """Return a list of all prime numbers up to and including n.
    >>> find_primes_list_comprehension(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> find_primes_list_comprehension(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> find_primes_list_comprehension(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    return [i for i in range(2, n+1) if is_prime(i)]

def find_primes_filter(n):
    """Return a list of all prime numbers up to and including n.
    >>> find_primes_filter(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> find_primes_filter(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> find_primes_filter(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    return list(filter(is_prime, range(2, n+1)))

def find_primes_set(n):
    """Return a set of all prime numbers up to and including n.
    >>> find_primes_set(20)
    {2, 3, 5, 7, 11, 13, 17, 19}
    >>> find_primes_set(30)
    {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
    >>> find_primes_set(50)
    {2, 3, 5, 7, 11, 13,