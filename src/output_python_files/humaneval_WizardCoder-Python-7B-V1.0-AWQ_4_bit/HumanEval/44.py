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
        raise ValueError("Input number must be positive")
    if x == 0:
        return '0'
    res = ''
    while x > 0:
        res = str(x % base) + res
        x //= base
    return res


def change_base_recursive(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base_recursive(8, 3)
    '22'
    >>> change_base_recursive(8, 2)
    '100'
    >>> change_base_recursive(7, 2)
    '11'
    """
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10")
    if x < 0:
        raise ValueError("Input number must be positive")
    if x == 0:
        return '0'
    return str(x % base) + change_base_recursive(x // base, base)


if __name__ == "__main__":
    import doctest
    doctest.testmod()