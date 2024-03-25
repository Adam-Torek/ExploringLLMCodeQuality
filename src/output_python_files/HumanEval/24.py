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
        if n % i == 0 and n / i > 1:
            return i


def smallest_divisor_of_sum(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0 and n / i > 1:
            return i


def smallest_divisor_of_sum_and_product(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum_and_product(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0 and n / i > 1:
            return i


def smallest_divisor_of_sum_and_product_2(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum_and_product_2(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0 and n / i > 1:
            return i


def smallest_divisor_of_sum_and_product_3(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum_and_product_3(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0 and n / i > 1:
            return i


def smallest_divisor_of_sum_and_product_4(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum_and_product_4(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0 and n / i > 1:
            return i


def smallest_divisor_of_sum_and_product_5(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum_and_product_5(15)
    3
    """
    for i in range(1, n + 1):
        if n % i == 0 and n / i > 1:
            return i


def smallest_divisor_of_sum_and_product_6(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_of_sum_and_product_6(15)
    3
    """