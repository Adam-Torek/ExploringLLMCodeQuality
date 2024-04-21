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
        raise ValueError("Base must be between 2 and 10")
    if x < 0:
        raise ValueError("Negative numbers are not supported")
    if x == 0:
        return "0"
    result = ""
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result


def change_base_v2(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base_v2(8, 3)
    '22'
    >>> change_base_v2(8, 2)
    '1000'
    >>> change_base_v2(7, 2)
    '111'
    """
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10")
    if x < 0:
        raise ValueError("Negative numbers are not supported")
    if x == 0:
        return "0"
    result = []
    while x > 0:
        result.append(str(x % base))
        x //= base
    return "".join(result[::-1])


def change_base_v3(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base_v3(8, 3)
    '22'
    >>> change_base_v3(8, 2)
    '1000'
    >>> change_base_v3(7, 2)
    '111'
    """
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10")
    if x < 0:
        raise ValueError("Negative numbers are not supported")
    if x == 0:
        return "0"
    result = []
    while x > 0:
        result.append(str(x % base))
        x //= base
    return "".join(result[::-1])


def change_base_v4(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base_v4(8, 3)
    '22'
    >>> change_base_v4(8, 2)
    '1000'
    >>> change_base_v4(7, 2)
    '111'
    """
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10")
    if x < 0:
        raise ValueError("Negative numbers are not supported")
    if x == 0:
        return "0"
    result = []
    while x > 0:
        result.append(str(x % base))
        x //= base
    return "".join(result[::-1])


def change_base_v5(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base_v5(8, 3)
    '22'
    >>> change_base_v5(8, 2)
    '1000'
    >>> change_base_v5(7, 2)
    '11