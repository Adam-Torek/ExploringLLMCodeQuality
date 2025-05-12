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


def truncate_number_to_decimal(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number_to_decimal(3.5)
    0.5
    """
    return number - int(number)


def truncate_number_to_int_with_decimal(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the integer part of the number.
    >>> truncate_number_to_int_with_decimal(3.5)
    3.0
    """
    return number - int(number)


def truncate_number_to_decimal_with_int(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the integer part of the number.
    >>> truncate_number_to_decimal_with_int(3.5)
    3.0
    """
    return number - int(number)


def truncate_number_to_decimal_with_int_and_decimal(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the integer part of the number.
    >>> truncate_number_to_decimal_with_int_and_decimal(3.5)
    3.0
    """
    return number - int(number)


def truncate_number_to_decimal_with_int_and_decimal_and_decimal(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the integer part of the number.
    >>> truncate_number_to_decimal_with_int_and_decimal_and_decimal(3.5)
    3.0
    """
    return number - int(number)


def truncate_number_to_decimal_with_int_and_decimal_and_decimal_and_decimal(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the integer part of the number.
    >>> truncate_number_to_decimal_with_int_and_decimal_and_decimal_and_decimal(3.5)
    3.0