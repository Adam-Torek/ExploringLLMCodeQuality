def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


def truncate_number_to_n_decimals(number: float, n: int) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number, truncated to n decimals.
    >>> truncate_number_to_n_decimals(3.5, 1)
    0.5
    >>> truncate_number_to_n_decimals(3.5, 2)
    0.5
    >>> truncate_number_to_n_decimals(3.5, 3)
    0.5
    """
    return truncate_number(number) * 10 ** n


def truncate_number_to_n_decimals_round(number: float, n: int) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number, truncated to n decimals, rounded
    to the nearest integer.
    >>> truncate_number_to_n_decimals_round(3.5, 1)
    1.0
    >>> truncate_number_to_n_decimals_round(3.5, 2)
    0.5
    >>> truncate_number_to_n_decimals_round(3.5, 3)
    0.5
    """
    return round(truncate_number(number) * 10 ** n) / 10 ** n


def truncate_number_to_n_decimals_round_up(number: float, n: int) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number, truncated to n decimals, rounded
    to the nearest integer, up.
    >>> truncate_number_to_n_decimals_round_up(3.5, 1)
    1.0
    >>> truncate_number_to_n_decimals_round_up(3.5, 2)
    1.0
    >>> truncate_number_to_n_decimals_round_up(3.5, 3)
    1.0
    """
    return round(truncate_number(number) * 10 ** n + 0.5) / 10 ** n


def truncate_number_to_n_decimals_round_down(number: float, n: int) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number, truncated to n decimals, rounded
    to the nearest integer, down.
    >>> truncate_number_to_n_decimals_round_down(3.5, 1)
    0.0
    >>> truncate_number_to_n_decimals_round_down(3.5, 2)
    0.0
    >>> truncate_number_to_n_decimals_round_down(3.5, 3)
    0.0
    """
    return round(truncate_number(number) * 10 ** n - 0.5) / 10 ** n


def truncate_number_to_n_decimals_round_half_up(number