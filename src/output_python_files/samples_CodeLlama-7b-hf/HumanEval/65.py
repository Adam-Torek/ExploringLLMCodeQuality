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


def circular_shift_test():
    """Test function for circular_shift."""
    print(circular_shift(12, 1))
    print(circular_shift(12, 2))
    print(circular_shift(12, 3))
    print(circular_shift(12, 4))
    print(circular_shift(12, 5))
    print(circular_shift(12, 6))
    print(circular_shift(12, 7))
    print(circular_shift(12, 8))
    print(circular_shift(12, 9))
    print(circular_shift(12, 10))
    print(circular_shift(12, 11))
    print(circular_shift(12, 12))
    print(circular_shift(12, 13))
    print(circular_shift(12, 14))
    print(circular_shift(12, 15))
    print(circular_shift(12, 16))
    print(circular_shift(12, 17))
    print(circular_shift(12, 18))
    print(circular_shift(12, 19))
    print(circular_shift(12, 20))
    print(circular_shift(12, 21))
    print(circular_shift(12, 22))
    print(circular_shift(12, 23))
    print(circular_shift(12, 24))
    print(circular_shift(12, 25))
    print(circular_shift(12, 26))
    print(circular_shift(12, 27))
    print(circular_shift(12, 28))
    print(circular_shift(12, 29))
    print(circular_shift(12, 30))
    print(circular_shift(12, 31))
    print(circular_shift(12, 32))
    print(circular_shift(12, 33))
    print(circular_shift(12, 34))
    print(circular_shift(12, 35))
    print(circular_shift(12, 36))
    print(circular_shift(12, 37))
    print(circular_shift(12, 38))
    print(circular_shift(12, 39))
    print(circular_shift(12, 40))
    print(circular_shift(12, 41))
    print(circular_shift(12, 42))
    print(circular_shift(12, 43))
    print(circular_shift(12, 44))
    print(circular_shift(12, 45))
    print(circular_shift(12, 46))
    print(circular_shift(12, 47))
    print(circular_shift(12, 48))
    print(circular_shift(12, 49))
    print(circular_shift(12, 50))
    print(circular_shift(12, 51))
    print(circular_shift(12, 52))
    print(circular_shift(12, 53))
    print(circular_shift(12, 54))
    print(circular_shift(12, 55))
    print(circular_shift(12,