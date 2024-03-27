def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


def truncate_number_to_int(number: float) -> int:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the integer part of the number.
    >>> truncate_number_to_int(3.5)
    3
    """
    return int(number)


def truncate_number_to_int_round_up(number: float) -> int:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the integer part of the number, rounded up.
    >>> truncate_number_to_int_round_up(3.5)
    4
    """
    return int(number + 0.5)


def truncate_number_to_int_round_down(number: float) -> int:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the integer part of the number, rounded down.
    >>> truncate_number_to_int_round_down(3.5)
    3
    """
    return int(number - 0.5)


def truncate_number_to_int_round_nearest(number: float) -> int:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the integer part of the number, rounded to the nearest integer.
    >>> truncate_number_to_int_round_nearest(3.5)
    4
    >>> truncate_number_to_int_round_nearest(3.2)
    3
    >>> truncate_number_to_int_round_nearest(3.8)
    4
    """
    return int(number + 0.5) if number % 1 >= 0.5 else int(number - 0.5)


def truncate_number_to_int_round_nearest_even(number: float) -> int:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the integer part of the number, rounded to the nearest even integer.
    >>> truncate_number_to_int_round_nearest_even(3.5)
    4
    >>> truncate_number_to_int_round_nearest_even(3.2)
    4
    >>> truncate_number_to_int_round_nearest_even(3.8)
    4
    >>> truncate_number_to_int_round_nearest_even(3.7)
    4
    >>> truncate_number_to_int_round_nearest_even(3.1)
    2
    """
    return int(number + 0.5) if number % 1 >= 0.5 else int(number - 0.5) if number % 1 >= 0.25 else int(number)


def truncate_number_to_int_round_nearest_odd(number: float) -> int:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the integer part of the number, rounded to the nearest odd integer.
    >>> truncate_