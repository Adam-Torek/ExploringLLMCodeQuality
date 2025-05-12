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
    if x == 0:
        return '0'
    result = ''
    while x != 0:
        x, d = divmod(x, base)
        result += str(d)
    return result[::-1]


def change_base_test():
    """Test for change_base function"""
    for x in [8, 7, 6, 5, 4, 3, 2, 1, 0]:
        for base in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            result = change_base(x, base)
            assert result == change_base(x, base)


if __name__ == '__main__':
    change_base_test()