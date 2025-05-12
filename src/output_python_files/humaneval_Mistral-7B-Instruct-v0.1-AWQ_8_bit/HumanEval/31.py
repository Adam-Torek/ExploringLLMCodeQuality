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
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime_number(n):
    """Return true if n is a prime number, and false otherwise.
    >>> is_prime_number(6)
    False
    >>> is_prime_number(101)
    True
    >>> is_prime_number(11)
    True
    >>> is_prime_number(13441)
    True
    >>> is_prime_number(61)
    True
    >>> is_prime_number(4)
    False
    >>> is_prime_number(1)
    False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime_numbers(n):
    """Return true if n is a prime number, and false otherwise.
    >>> is_prime_numbers(6)
    False
    >>> is_prime_numbers(101)
    True
    >>> is_prime_numbers(11)
    True
    >>> is_prime_numbers(13441)
    True
    >>> is_prime_numbers(61)
    True
    >>> is_prime_numbers(4)
    False
    >>> is_prime_numbers(1)
    False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime_number_list(n):
    """Return true if n is a prime number, and false otherwise.
    >>> is_prime_number_list(6)
    False
    >>> is_prime_number_list(101)
    True
    >>> is_prime_number_list(11)
    True
    >>> is_prime_number_list(13441)
    True
    >>> is_prime_number_list(61)
    True
    >>> is_prime_number_list(4)
    False
    >>> is_prime_number_list(1)
    False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime_number_list_of_numbers(n):
    """Return true if n is a prime number, and false otherwise.
    >>> is_prime_number_list_of_numbers(6)
    False
    >>> is_prime_number_list_of_numbers(101)
    True
    >>> is_prime_number_list_of_numbers(11)
    True
    >>> is_prime_number_list_of_numbers(13441)
    True
    >>> is_prime_number_list_of_