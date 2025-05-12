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
    """Test case for circular_shift"""
    print("x =", x, "shift =", shift, "result =", circular_shift(x, shift))


if __name__ == "__main__":
    circular_shift_test_case(12, 1)
    circular_shift_test_case(12, 2)
    circular_shift_test_case(12, 3)
    circular_shift_test_case(12, 4)
    circular_shift_test_case(12, 5)
    circular_shift_test_case(12, 6)
    circular_shift_test_case(12, 7)
    circular_shift_test_case(12, 8)
    circular_shift_test_case(12, 9)
    circular_shift_test_case(12, 10)
    circular_shift_test_case(12, 11)
    circular_shift_test_case(12, 12)
    circular_shift_test_case(12, 13)
    circular_shift_test_case(12, 14)
    circular_shift_test_case(12, 15)
    circular_shift_test_case(12, 16)
    circular_shift_test_case(12, 17)
    circular_shift_test_case(12, 18)
    circular_shift_test_case(12, 19)
    circular_shift_test_case(12, 20)
    circular_shift_test_case(12, 21)
    circular_shift_test_case(12, 22)
    circular_shift_test_case(12, 23)
    circular_shift_test_case(12, 24)
    circular_shift_test_case(12, 25)
    circular_shift_test_case(12, 26)
    circular_shift_test_case(12, 27)
    circular_shift_test_case(12, 28)
    circular_shift_test_case(12, 29)
    circular_shift_test_case(12, 30)
    circular_shift_test_case(12, 31)
    circular_shift_test_case(12, 32)
    circular_shift_test_case(12, 33)
    circular_shift_test_case(12, 34)
    circular_shift_test_case(12, 35)
    circular_shift_test_case(12, 36)
    circular_shift_test_case(12, 37)
    circular_shift_test_case(12, 38)
    circular_shift_test_case(12, 39)
    circular_shift_test_case(12, 40)
    circular_shift_test_case(12, 41)
    circular_shift_test_case(12, 42)
    circular_shift_test_case(12, 43)
    circular_shift_test_case(12, 44)
    circular_shift_test_case(12, 45)
    circular_shift_test_case(12, 46)
    circular_shift_test_case(12, 47)
    circular_shift_test_case(12, 48)
    circular_shift_test_case(12, 49)
    circular_shift_test_case(12,