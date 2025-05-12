"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""
def sum_digits(n):
    """
    :param n: non-negative integer
    :return: sum of digits of n
    """
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

assert sum_digits(345) == 12
assert sum_digits(0) == 0
assert sum_digits(123) == 6
assert sum_digits(1024) == 11
assert sum_digits(12345) == 15
assert sum_digits(123456) == 21
assert sum_digits(1234567) == 27
assert sum_digits(12345678) == 36
assert sum_digits(123456789) == 45
assert sum_digits(1234567890) == 54
assert sum_digits(12345678901) == 65
assert sum_digits(123456789012) == 77
assert sum_digits(1234567890123) == 89
assert sum_digits(12345678901234) == 101
assert sum_digits(123456789012345) == 112
assert sum_digits(1234567890123456) == 123
assert sum_digits(12345678901234567) == 134
assert sum_digits(123456789012345678) == 145
assert sum_digits(1234567890123456789) == 156
assert sum_digits(12345678901234567890) == 167
assert sum_digits(123456789012345678901) == 178
assert sum_digits(1234567890123456789012) == 189
assert sum_digits(12345678901234567890123) == 200
assert sum_digits(123456789012345678901234) == 211
assert sum_digits(1234567890123456789012345) == 222
assert sum_digits(12345678901234567890123456) == 233
assert sum_digits(123456789012345678901234567) == 244
assert sum_digits(1234567890123456789012345678) == 255
assert sum_digits(12345678901234567890123456789) == 266
assert sum_digits(123456789012345678901234567890) == 277
assert sum_digits(1234567890123456789012345678901) == 288
assert sum_digits(12345678901234567890123