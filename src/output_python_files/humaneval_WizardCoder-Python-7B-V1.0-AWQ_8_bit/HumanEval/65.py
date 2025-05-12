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
    """Return True if n is prime, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



def is_circular_prime(n):
    """Return True if n is a circular prime, False otherwise."""
    circular_n = int(circular_shift(n, 1))
    return is_prime(n) and all(is_prime(int(circular_shift(circular_n, i)) for i in range(1, len(str(n))) if i != 0) and n != 1)



def count_circular_primes(n):
    """Return the number of circular primes less than n."""
    return sum(1 for i in range(2, n) if is_circular_prime(i))



if __name__ == "__main__":
    print(count_circular_primes(100000000))