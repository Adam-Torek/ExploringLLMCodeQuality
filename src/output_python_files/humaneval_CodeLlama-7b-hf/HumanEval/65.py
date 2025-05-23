def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    return str(int(str(x)[shift:] + str(x)[:shift]))


def circular_shift_list(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a list.
    If shift > number of digits, return digits reversed.
    >>> circular_shift_list(12, 1)
    [2, 1]
    >>> circular_shift_list(12, 2)
    [1, 2]
    """
    return list(map(int, str(x)[shift:] + str(x)[:shift]))


def circular_shift_list_2(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a list.
    If shift > number of digits, return digits reversed.
    >>> circular_shift_list_2(12, 1)
    [2, 1]
    >>> circular_shift_list_2(12, 2)
    [1, 2]
    """
    return [int(x) for x in str(x)[shift:] + str(x)[:shift]]


def circular_shift_list_3(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a list.
    If shift > number of digits, return digits reversed.
    >>> circular_shift_list_3(12, 1)
    [2, 1]
    >>> circular_shift_list_3(12, 2)
    [1, 2]
    """
    return [int(x) for x in str(x)[shift:] + str(x)[:shift]]


def circular_shift_list_4(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a list.
    If shift > number of digits, return digits reversed.
    >>> circular_shift_list_4(12, 1)
    [2, 1]
    >>> circular_shift_list_4(12, 2)
    [1, 2]
    """
    return [int(x) for x in str(x)[shift:] + str(x)[:shift]]


def circular_shift_list_5(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a list.
    If shift > number of digits, return digits reversed.
    >>> circular_shift_list_5(12, 1)
    [2, 1]
    >>> circular_shift_list_5(12, 2)
    [1, 2]
    """
    return [int(x) for x in str(x)[shift:] + str(x)[:shift]]


def circular_shift_list_6(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a list.
    If shift > number of digits, return digits reversed.
    >>> circular_shift_list_6