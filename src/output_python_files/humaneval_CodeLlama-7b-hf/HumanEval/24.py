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


def smallest_divisor_of_product(n: int, m: int) -> int:
    """ For a given number n and m, find the smallest number that divides both n and m evenly
    >>> smallest_divisor_of_product(15, 10)
    5
    """
    return largest_divisor(n * m)


def smallest_divisor_of_sum(n: int, m: int) -> int:
    """ For a given number n and m, find the smallest number that divides both n and m evenly
    >>> smallest_divisor_of_sum(15, 10)
    3
    """
    return smallest_divisor(n + m)


def smallest_divisor_of_difference(n: int, m: int) -> int:
    """ For a given number n and m, find the smallest number that divides both n and m evenly
    >>> smallest_divisor_of_difference(15, 10)
    5
    """
    return smallest_divisor(n - m)


def smallest_divisor_of_quotient(n: int, m: int) -> int:
    """ For a given number n and m, find the smallest number that divides both n and m evenly
    >>> smallest_divisor_of_quotient(15, 10)
    3
    """
    return smallest_divisor(n // m)


def smallest_divisor_of_remainder(n: int, m: int) -> int:
    """ For a given number n and m, find the smallest number that divides both n and m evenly
    >>> smallest_divisor_of_remainder(15, 10)
    5
    """
    return smallest_divisor(n % m)


def smallest_divisor_of_quotient_and_remainder(n: int, m: int) -> int:
    """ For a given number n and m, find the smallest number that divides both n and m evenly
    >>> smallest_divisor_of_quotient_and_remainder(15, 10)
    5
    """
    return smallest_divisor(n // m % n)


def smallest_divisor_of_quotient_and_remainder_and_difference(n: int, m: int) -> int:
    """ For a given number n and m, find the smallest number that divides both n and m evenly
    >>> smallest_divisor_of_quotient_and_remainder_and_difference(15, 10)
    5
    """
    return smallest_divisor(n // m % n - n % m)


def smallest_divisor_of_quotient_and_remainder_and_difference_and_product(n: int, m: int) -> int:
    """ For a given number n and m, find the smallest number that divides both n and m evenly
    >>> smallest_divisor_of_quotient_and_remainder_and_difference_and_product(15, 10)