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
        raise ValueError("Invalid base number.")
    if x == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = ""
    while x != 0:
        x, index = divmod(x, base)
        result += digits[index]
    return result[::-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()</s>