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
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    if x < 0:
        raise ValueError("Input number must be positive")
    result = ""
    while x > 0:
        digit = x % base
        result = str(digit) + result
        x = x // base
    return result


def test_change_base():
    assert change_base(8, 3) == "22"
    assert change_base(8, 2) == "100"
    assert change_base(7, 2) == "11"
    assert change_base(10, 2) == "1010"
    assert change_base(10, 8) == "12"
    assert change_base(10, 10) == "10"
    assert change_base(10, 16) == "A"
    assert change_base(10, 16) == "A"
    assert change_base(10, 17) == "A"
    assert change_base(10, 10) == "10"
    assert change_base(10, 11) == "A"
    assert change_base(10, 12) == "A"
    assert change_base(10, 13) == "A"
    assert change_base(10, 14) == "A"
    assert change_base(10, 15) == "A"
    assert change_base(10, 16) == "A"
    assert change_base(10, 17) == "A"
    assert change_base(10, 18) == "A"
    assert change_base(10, 19) == "A"
    assert change_base(10, 20) == "A"
    assert change_base(10, 21) == "A"
    assert change_base(10, 22) == "A"
    assert change_base(10, 23) == "A"
    assert change_base(10, 24) == "A"
    assert change_base(10, 25) == "A"
    assert change_base(10, 26) == "A"
    assert change_base(10, 27) == "A"
    assert change_base(10, 28) == "A"
    assert change_base(10, 29) == "A"
    assert change_base(10, 30) == "A"
    assert change_base(10, 31) == "A"
    assert change_base(10, 32) == "A"
    assert change_base(10, 33) == "A"
    assert change_base(10, 34) == "A"
    assert change_base(10, 35) == "A"
    assert change_base(10, 36) == "A"
    assert change_base(10, 37) == "A"
    assert change_base(10, 38) == "A"
    assert change_base(10, 39) == "A"
    assert change_base(10, 40) == "A"
    assert change_base(10, 41) == "A"