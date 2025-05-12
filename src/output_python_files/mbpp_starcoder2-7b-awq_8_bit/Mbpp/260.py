"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""

def newman_prime(n):
    """
    >>> newman_prime(3)
    7
    >>> newman_prime(10)
    31
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return newman_prime(n-1) + newman_prime(n-2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/README.md
# newman_prime
Write a function to find the nth newman–shanks–williams prime number.