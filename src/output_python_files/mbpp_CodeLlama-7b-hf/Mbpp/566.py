"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""


def sum_digits(n):
    """
    :param n: non-negative integer
    :return: sum of the digits of n
    """
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)


if __name__ == '__main__':
    print(sum_digits(345))
    print(sum_digits(123456789))
    print(sum_digits(1234567890))
    print(sum_digits(12345678901))
    print(sum_digits(123456789012))
    print(sum_digits(1234567890123))
    print(sum_digits(12345678901234))
    print(sum_digits(123456789012345))
    print(sum_digits(1234567890123456))
    print(sum_digits(12345678901234567))
    print(sum_digits(123456789012345678))
    print(sum_digits(1234567890123456789))
    print(sum_digits(12345678901234567890))
    print(sum_digits(123456789012345678901))
    print(sum_digits(1234567890123456789012))
    print(sum_digits(12345678901234567890123))
    print(sum_digits(123456789012345678901234))
    print(sum_digits(1234567890123456789012345))
    print(sum_digits(12345678901234567890123456))
    print(sum_digits(123456789012345678901234567))
    print(sum_digits(1234567890123456789012345678))
    print(sum_digits(12345678901234567890123456789))
    print(sum_digits(123456789012345678901234567890))
    print(sum_digits(1234567890123456789012345678901))
    print(sum_digits(12345678901234567890123456789012))
    print(sum_digits(123456789012345678901234567890123))
    print(sum_digits(1234567890123456789012345678901234))
    print(sum_digits(12345678901234567890123456789012345))
    print(sum_digits(1234567890123