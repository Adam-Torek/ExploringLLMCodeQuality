def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


def truncate_number_to_decimals(number: float, decimals: int) -> float:
    """ Given a positive floating point number and an integer, it can be
    decomposed into and integer part (largest integer smaller than given
    number) and decimals (leftover part always smaller than 1).

    Return the decimal part of the number, truncated to the given number of
    decimals.
    >>> truncate_number_to_decimals(3.5, 1)
    0.5
    >>> truncate_number_to_decimals(3.5, 2)
    0.5
    """
    return truncate_number(number) * (10 ** decimals)


def truncate_number_to_decimals_round(number: float, decimals: int) -> float:
    """ Given a positive floating point number and an integer, it can be
    decomposed into and integer part (largest integer smaller than given
    number) and decimals (leftover part always smaller than 1).

    Return the decimal part of the number, truncated to the given number of
    decimals, rounded to the nearest number.
    >>> truncate_number_to_decimals_round(3.5, 1)
    0.5
    >>> truncate_number_to_decimals_round(3.5, 2)
    0.5
    """
    return round(truncate_number(number) * (10 ** decimals), decimals)


def truncate_number_to_decimals_round_half_up(number: float, decimals: int) -> float:
    """ Given a positive floating point number and an integer, it can be
    decomposed into and integer part (largest integer smaller than given
    number) and decimals (leftover part always smaller than 1).

    Return the decimal part of the number, truncated to the given number of
    decimals, rounded to the nearest number.
    If the number is exactly halfway between two numbers, it will be rounded
    up.
    >>> truncate_number_to_decimals_round_half_up(3.5, 1)
    1.0
    >>> truncate_number_to_decimals_round_half_up(3.5, 2)
    1.0
    """
    return round(truncate_number(number) * (10 ** decimals), decimals)


def truncate_number_to_decimals_round_half_down(number: float, decimals: int) -> float:
    """ Given a positive floating point number and an integer, it can be
    decomposed into and integer part (largest integer smaller than given
    number) and decimals (leftover part always smaller than 1).

    Return the decimal part of the number, truncated to the given number of
    decimals, rounded to the nearest number.
    If the number is exactly halfway between two numbers, it will be rounded
    down.
    >>> truncate_number_to_decimals_round_half_down(3.5, 1)
    0.0
    >>> truncate_number_to_decimals_round_half_down(3.5, 2)
    0.0
    """
    return round(truncate_number(number) * (10 ** decimals), decimals)


def truncate_number_to_decimals_round_half_even(number: float, decimals: int) -> float:
    """ Given a positive floating point number and an integer, it can be