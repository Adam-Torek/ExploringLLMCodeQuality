def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n, 0, -1):
        if n % i == 0:
            return i


def smallest_divisor(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0:
            return i


def smallest_divisor_of_product(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_product(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0:
            return i


def smallest_divisor_of_sum(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0:
            return i


def smallest_divisor_of_sum_of_divisors(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum_of_divisors(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0:
            return i


def smallest_divisor_of_sum_of_divisors_of_sum(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum_of_divisors_of_sum(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0:
            return i


def smallest_divisor_of_sum_of_divisors_of_sum_of_divisors(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum_of_divisors_of_sum_of_divisors(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0:
            return i


def smallest_divisor_of_sum_of_divisors_of_sum_of_divisors_of_sum(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum_of_divisors_of_sum_of_divisors_of_sum(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0:
            return i


def smallest_divisor_of_sum_of_divisors_of_sum_of_divisors_of_sum_of_divisors(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum_of_divisors_of_sum_of_divisors_of_sum_of_divisors(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0:
            return i


def smallest_divisor_of_sum_of_divisors_of_sum_of_divis