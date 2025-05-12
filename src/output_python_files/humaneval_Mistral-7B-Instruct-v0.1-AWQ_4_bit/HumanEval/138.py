def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 0:
        return False
    for i in range(2, n):
        if i % 2 == 0:
            if n - i == 4 * i:
                return True
    return False


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive odd numbers
    Example
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(6) == False
    is_equal_to_sum_odd(8) == False
    is_equal_to_sum_odd(10) == True
    """
    if n % 2 == 0:
        return False
    for i in range(1, n):
        if i % 2 == 1:
            if n - i == 4 * i:
                return True
    return False


def is_equal_to_sum_even_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even and odd numbers
    Example
    is_equal_to_sum_even_odd(4) == False
    is_equal_to_sum_even_odd(6) == False
    is_equal_to_sum_even_odd(8) == False
    is_equal_to_sum_even_odd(10) == True
    """
    if n % 2 == 0:
        return False
    for i in range(1, n):
        if i % 2 == 1:
            if n - i == 4 * i:
                return True
    return False


def is_equal_to_sum_even_odd_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even and even numbers
    Example
    is_equal_to_sum_even_odd_even(4) == False
    is_equal_to_sum_even_odd_even(6) == False
    is_equal_to_sum_even_odd_even(8) == False
    is_equal_to_sum_even_odd_even(10) == False
    is_equal_to_sum_even_odd_even(12) == True
    """
    if n % 2 == 0:
        return False
    for i in range(1, n):
        if i % 2 == 0:
            if n - i == 4 * i:
                return True
    return False


def is_equal_to_sum_even_odd_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even and odd numbers
    Example
    is_equal_to_sum_even_odd_odd(4) == False
    is_equal_to_sum_even_odd_odd(6) == False
    is_equal_to_sum_even_odd_odd(8) == False
    is_equal_to_sum_even_odd_odd(10) == False
    is_equal_to_sum_even_odd_odd(12) == False
    is_equal_to_sum_even_odd_odd(14) == True
    """
    if n % 2 == 0:
        return False
    for i in range(1, n):
        if i % 2 == 1:
            if n - i == 4 * i:
                return True
    return False


def is_equal_to_sum_even