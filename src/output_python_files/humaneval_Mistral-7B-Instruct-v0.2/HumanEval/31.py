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


def prime_sum(n):
    """Return the sum of all prime numbers less than or equal to n.
    >>> prime_sum(10)
    17
    >>> prime_sum(100)
    1683
    >>> prime_sum(1000)
    76127
    >>> prime_sum(10000)
    6679730
    >>> prime_sum(100000)
    515127127
    """
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return sum(primes)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(prime_sum(n))