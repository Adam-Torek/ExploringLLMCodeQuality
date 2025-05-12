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
    for i in range(1, n):
        if n % i == 0:
            return i


def smallest_divisor_for_range(n: int, start: int, end: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_for_range(15, 2, 5)
    3
    """
    for i in range(start, end):
        if n % i == 0:
            return i


def smallest_divisor_for_range_with_step(n: int, start: int, end: int, step: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_for_range_with_step(15, 2, 5, 2)
    3
    """
    for i in range(start, end, step):
        if n % i == 0:
            return i


def smallest_divisor_for_range_with_step_and_start(n: int, start: int, end: int, step: int, start_value: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_for_range_with_step_and_start(15, 2, 5, 2, 3)
    5
    """
    for i in range(start_value, end, step):
        if n % i == 0:
            return i


def smallest_divisor_for_range_with_step_and_start_and_end(n: int, start: int, end: int, step: int, start_value: int,
                                                           end_value: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_for_range_with_step_and_start_and_end(15, 2, 5, 2, 3, 5)
    5
    """
    for i in range(start_value, end_value, step):
        if n % i == 0:
            return i


def smallest_divisor_for_range_with_step_and_start_and_end_and_step(n: int, start: int, end: int, step: int,
                                                                    start_value: int, end_value: int,
                                                                    step_value: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor_for_range_with_step_and_start_and_end_and_step(15, 2, 5, 2, 3, 5, 2)
    5
    """
    for i in range(start_value, end_value, step_value):
        if n % i == 0:
            return i


def smallest_divisor_for_range_with_step_and_start_and_end_and_step_and_start(n: int, start: int, end: int,