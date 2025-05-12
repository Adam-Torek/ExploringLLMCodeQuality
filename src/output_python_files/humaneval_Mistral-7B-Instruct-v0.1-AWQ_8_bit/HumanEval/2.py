def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        return -number
    integer_part = int(number)
    return number - integer_part


def truncate_number_with_precision(number: float, precision: int) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number with a given precision.
    >>> truncate_number_with_precision(3.5, 2)
    0.5
    """
    if number < 0:
        return -number
    integer_part = int(number)
    return number - integer_part


def truncate_number_with_precision_and_rounding(number: float, precision: int, rounding: str) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number with a given precision and rounding.
    >>> truncate_number_with_precision_and_rounding(3.5, 2, 'round')
    0.5
    >>> truncate_number_with_precision_and_rounding(3.5, 2, 'ceil')
    0.5
    >>> truncate_number_with_precision_and_rounding(3.5, 2, 'floor')
    0.5
    """
    if number < 0:
        return -number
    integer_part = int(number)
    return number - integer_part


def truncate_number_with_precision_and_rounding_and_sign(number: float, precision: int, rounding: str, sign: str) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number with a given precision and rounding.
    >>> truncate_number_with_precision_and_rounding_and_sign(3.5, 2, 'round', '+')
    0.5
    >>> truncate_number_with_precision_and_rounding_and_sign(3.5, 2, 'ceil', '+')
    0.5
    >>> truncate_number_with_precision_and_rounding_and_sign(3.5, 2, 'floor', '+')
    0.5
    >>> truncate_number_with_precision_and_rounding_and_sign(3.5, 2, 'round', '-')
    0.5
    >>> truncate_number_with_precision_and_rounding_and_sign(3.5, 2, 'ceil', '-')
    0.5
    >>> truncate_number_with_precision_and_rounding_and_sign(3.5, 2, 'floor', '-')
    0.5
    """
    if number < 0:
        return -number
    integer_part = int(number)
    return number - integer_part


def truncate_number_with_precision_and_rounding_and_sign_and_rounding_mode(number: float, precision: int, rounding: str, sign: str, rounding_mode: str) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number with a given precision and rounding.
    >>> truncate_number_with_precision_