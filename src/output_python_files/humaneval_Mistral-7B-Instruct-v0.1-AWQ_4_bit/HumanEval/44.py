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
    if base < 2:
        raise ValueError("base must be greater than 1")
    if base == 10:
        return str(x)
    if x == 0:
        return '0'
    result = ''
    while x != 0:
        x, d = divmod(x, base)
        result += str(d)
    return result[::-1]


def change_base_test():
    """Test for change_base function"""
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(10, 2) == '1000'
    assert change_base(10, 10) == '10'
    assert change_base(1, 10) == '1'
    assert change_base(1, 2) == '11'
    assert change_base(1, 1) == '1'
    assert change_base(0, 10) == '0'
    assert change_base(0, 2) == '0'
    assert change_base(0, 1) == '0'
    assert change_base(100, 10) == '100'
    assert change_base(100, 2) == '11110'
    assert change_base(100, 10) == '100'
    assert change_base(100, 1) == '100'
    assert change_base(100, 100) == '100'
    assert change_base(100, 1000) == '100'
    assert change_base(100, 10000) == '100'
    assert change_base(100, 100000) == '100'
    assert change_base(100, 1000000) == '100'
    assert change_base(100, 10000000) == '100'
    assert change_base(100, 100000000) == '100'
    assert change_base(100, 1000000000) == '100'
    assert change_base(100, 10000000000) == '100'
    assert change_base(100, 100000000000) == '100'
    assert change_base(100, 1000000000000) == '100'
    assert change_base(100, 10000000000000) == '100'
    assert change_base(100, 100000000000000) == '100'
    assert change_base(100, 1000000000000000) == '100'
    assert change_base(100, 10000000000000000) == '100'
    assert change_base(100, 10