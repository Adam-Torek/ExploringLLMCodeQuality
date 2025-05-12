def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = str(x)
    shift = shift % len(digits)
    return digits[-shift:] + digits[:-shift]



def is_prime(n):
    """Return True if n is prime, False otherwise.
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



def is_circular_prime(n):
    """Return True if n is a circular prime, False otherwise.
    >>> is_circular_prime(12321)
    True
    >>> is_circular_prime(13)
    False
    """
    return all(is_prime(int(circular_shift(n, i)) for i in range(len(str(n))) if n != 0)



def circular_primes(n):
    """Return the number of circular primes less than n.
    >>> circular_primes(100)
    55
    """
    return sum(1 for i in range(1, n) if is_circular_prime(i))



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(circular_primes(100000000))