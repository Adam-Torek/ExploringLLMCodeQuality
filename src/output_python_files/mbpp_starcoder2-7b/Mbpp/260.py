"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""

def newman_prime(n):
    """
    >>> newman_prime(3)
    7
    >>> newman_prime(4)
    11
    >>> newman_prime(5)
    17
    >>> newman_prime(6)
    29
    >>> newman_prime(7)
    41
    >>> newman_prime(8)
    59
    >>> newman_prime(9)
    71
    >>> newman_prime(10)
    97
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return newman_prime(n-1) + 2 * newman_prime(n-2) - 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/hw03/hw03.py
"""
Homework 3
"""

def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(12)
    False
    >>> is_prime(11)
    True
    """
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False
        return True

def nth_prime(n):
    """
    >>> nth_prime(1)
    2
    >>> nth_prime(2)
    3
    >>> nth_prime(3)
    5
    >>> nth_prime(4)
    7
    >>> nth_prime(5)
    11
    >>> nth_prime(6)
    13
    >>> nth_prime(7)
    17
    >>> nth_prime(8)
    19
    >>> nth_prime(9)
    23
    >>> nth_prime(10)
    29
    """
    count = 0
    i = 2
    while count < n:
        if is_prime(i):
            count += 1
        i += 1
    return i - 1

def prime_factors(n):
    """
    >>> prime_factors(10)
    [2, 5]
    >>> prime_factors(14)
    [2, 7]
    >>> prime_factors(15)
    [3, 5]
    >>> prime_factors(21)
    [3, 7]
    >>> prime_factors(25)
    [5, 5]
    >>> prime_factors(27)
    [3, 3, 3]
    >>> prime_factors(100)
    [2, 2, 5, 5]
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_palindrome(n):
    """
    >>> is_palindrome(121)
    True
    >>> is_palindrome(123)
    False
    >>> is_palindrome(1001)
    True
    """
    return str(n) == str(n)[::-1]

def nth_palindromic_prime(n):
    """
    >>> nth_palindromic_prime(1)
    2
    >>> nth_palindromic_prime(2)
    11
    >>> nth_palindromic_prime(3)
    101
    >>> nth_palindromic_prime(4)
    131
    >>> nth_palindromic_prime(5)
    1001
    >>> nth_palindromic_prime(6)
    10301
    >>> nth_palindromic_prime(7)
    100001
    >>> nth_palindromic_prime(8)
    1030301
    >>> nth_palindromic_prime(9)
    100000001
    >>> nth_palindromic_prime(10)
    10030