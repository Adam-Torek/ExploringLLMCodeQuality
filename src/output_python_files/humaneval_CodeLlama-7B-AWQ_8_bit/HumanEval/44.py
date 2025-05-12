def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base < 2 or base > 10:
        raise ValueError("base must be between 2 and 10")
    if x < 0:
        raise ValueError("x must be positive")
    if x == 0:
        return "0"
    result = ""
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result


def change_base_2(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base_2(8, 3)
    '22'
    >>> change_base_2(8, 2)
    '1000'
    >>> change_base_2(7, 2)
    '111'
    """
    if base < 2 or base > 10:
        raise ValueError("base must be between 2 and 10")
    if x < 0:
        raise ValueError("x must be positive")
    if x == 0:
        return "0"
    result = ""
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result


def change_base_3(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base_3(8, 3)
    '22'
    >>> change_base_3(8, 2)
    '1000'
    >>> change_base_3(7, 2)
    '111'
    """
    if base < 2 or base > 10:
        raise ValueError("base must be between 2 and 10")
    if x < 0:
        raise ValueError("x must be positive")
    if x == 0:
        return "0"
    result = ""
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result


def change_base_4(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base_4(8, 3)
    '22'
    >>> change_base_4(8, 2)
    '1000'
    >>> change_base_4(7, 2)
    '111'
    """
    if base < 2 or base > 10:
        raise ValueError("base must be between 2 and 10")
    if x < 0:
        raise ValueError("x must be positive")
    if x == 0:
        return "0"
    result = ""
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result


def change_base_5(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base_5(8, 3)
    '22'
    >>> change_base_5(8, 2)
    '1000'
    >>> change_base_5(7, 2)
    '111'
    """
    if base < 2 or base > 10:
        raise ValueError("base must be between 2 and 10")
    if x < 0:
        raise ValueError("x must be positive")