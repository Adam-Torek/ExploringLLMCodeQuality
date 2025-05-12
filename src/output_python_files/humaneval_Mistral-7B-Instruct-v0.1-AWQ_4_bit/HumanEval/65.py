def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x = abs(x)
    digits = str(x)
    if shift > len(digits):
        digits = digits[1:] + digits[0]
    return digits[shift:] + digits[:shift]


def circular_shift_test():
    """Test circular_shift function"""
    for x in range(1, 11):
        for shift in range(1, 11):
            result = circular_shift(x, shift)
            assert result == str(x) + result[:shift - 1], "Test failed"


if __name__ == '__main__':
    circular_shift_test()