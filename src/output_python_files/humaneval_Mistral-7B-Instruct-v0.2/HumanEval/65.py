def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = str(abs(x))[::-1] # reverse digits
    shift = shift % len(digits)
    return digits[shift:] + digits[:shift]

# test
print(circular_shift(12345, 1))
print(circular_shift(12345, 2))
print(circular_shift(12345, 3))
print(circular_shift(12345, 4))
print(circular_shift(12345, 5))
print(circular_shift(12345, 6))
print(circular_shift(12345, 7))
print(circular_shift(12345, 8))
print(circular_shift(12345, 9))
print(circular_shift(12345, 10))
print(circular_shift(12345, 11))
print(circular_shift(12345, 12))
print(circular_shift(12345, 13))
print(circular_shift(12345, 14))
print(circular_shift(12345, 15))
print(circular_shift(12345, 16))
print(circular_shift(12345, 17))
print(circular_shift(12345, 18))
print(circular_shift(12345, 19))
print(circular_shift(12345, 20))
print(circular_shift(12345, 21))
print(circular_shift(12345, 22))
print(circular_shift(12345, 23))
print(circular_shift(12345, 24))
print(circular_shift(12345, 25))
print(circular_shift(12345, 26))
print(circular_shift(12345, 27))
print(circular_shift(12345, 28))
print(circular_shift(12345, 29))
print(circular_shift(12345, 30))
print(circular_shift(12345, 31))
print(circular_shift(12345, 32))
print(circular_shift(12345, 33))
print(circular_shift(12345, 34))
print(circular_shift(12345, 35))
print(circular_shift(12345, 36))
print(circular_shift(12345, 37))
print(circular_shift(12345, 38))
print(circular_shift(12345, 39))
print(circular_shift(12345, 40))
print(circ