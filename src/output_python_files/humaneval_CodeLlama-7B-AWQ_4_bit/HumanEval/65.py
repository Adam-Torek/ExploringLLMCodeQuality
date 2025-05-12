def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Your code here
    return str(x)[shift:] + str(x)[:shift]


def circular_shift_test_case(x, shift):
    """Test case for circular_shift.
    >>> circular_shift_test_case(12, 1)
    True
    >>> circular_shift_test_case(12, 2)
    True
    >>> circular_shift_test_case(12, 3)
    False
    """
    return circular_shift(x, shift) == str(x)[shift:] + str(x)[:shift]


def circular_shift_test():
    """Test function for circular_shift.
    >>> circular_shift_test()
    True
    """
    return (circular_shift_test_case(12, 1) and
            circular_shift_test_case(12, 2) and
            circular_shift_test_case(12, 3))


def main():
    """Read in the number of test cases and run the test cases.
    >>> main()
    True
    """
    return (circular_shift_test() and
            circular_shift(12, 1) == "21" and
            circular_shift(12, 2) == "12" and
            circular_shift(12, 3) == "123" and
            circular_shift(123, 1) == "231" and
            circular_shift(123, 2) == "312" and
            circular_shift(123, 3) == "123" and
            circular_shift(123, 4) == "312" and
            circular_shift(123, 5) == "231" and
            circular_shift(123, 6) == "123" and
            circular_shift(123, 7) == "123" and
            circular_shift(123, 8) == "123" and
            circular_shift(123, 9) == "123" and
            circular_shift(123, 10) == "123" and
            circular_shift(123, 11) == "123" and
            circular_shift(123, 12) == "123" and
            circular_shift(123, 13) == "123" and
            circular_shift(123, 14) == "123" and
            circular_shift(123, 15) == "123" and
            circular_shift(123, 16) == "123" and
            circular_shift(123, 17) == "123" and
            circular_shift(123, 18) == "123" and
            circular_shift(123, 19) == "123" and
            circular_shift(123, 20) == "123" and
            circular_shift(123, 21) == "123" and
            circular_shift(123