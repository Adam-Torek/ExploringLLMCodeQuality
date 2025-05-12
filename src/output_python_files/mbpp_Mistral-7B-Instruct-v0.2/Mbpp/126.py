"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""
from math import gcd

def sum_of_common_divisors(num1, num2):
    """
    Function to find the sum of common divisors of two given numbers
    :param num1: first number
    :param num2: second number
    :return: sum of common divisors
    """
    common_divisors = []
    i = 1
    while i <= min(num1, num2):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)
        i += 1
    return sum(common_divisors)

assert sum_of_common_divisors(10, 15) == 6
assert sum_of_common_divisors(12, 18) == 12
assert sum_of_common_divisors(17, 23) == 1
assert sum_of_common_divisors(25, 36) == 15
assert sum_of_common_divisors(15, 20) == 15
assert sum_of_common_divisors(10, 20) == 10
assert sum_of_common_divisors(20, 10) == 10
assert sum_of_common_divisors(1, 1) == 1
assert sum_of_common_divisors(1, 2) == 1
assert sum_of_common_divisors(2, 1) == 1
assert sum_of_common_divisors(1, 2) == 1
assert sum_of_common_divisors(2, 2) == 2
assert sum_of_common_divisors(2, 4) == 2
assert sum_of_common_divisors(4, 2) == 2
assert sum_of_common_divisors(4, 4) == 4
assert sum_of_common_divisors(4, 6) == 4
assert sum_of_common_divisors(6, 4) == 4
assert sum_of_common_divisors(6, 6) == 6
assert sum_of_common_divisors(6, 8) == 6
assert sum_of_common_divisors(8, 6) == 6
assert sum_of_common_divisors(8, 8) == 8
assert sum_of_common_divisors(8, 12) == 8
assert sum_of_common_divisors(12, 8) == 8
assert sum_of_common_divisors(12, 12) == 12
assert sum_of_common_divisors(12, 18) == 12
assert sum_of_common_divisors(18, 12) == 12
assert sum_of_common_divisors(18, 18) == 18
assert sum_of_common_divisors(18, 24) == 18
assert sum_of_common_divisors(24, 18) == 18
assert sum_of_common_divisors(24, 24) == 24
assert sum_of_common_divisors(24, 36) == 24
assert sum_of_common_divisors(36, 24) == 24
assert sum_of_common_divisors(36, 36) == 36
assert sum_of_common_divisors(36, 48) == 36
assert sum_of_common_divisors(48, 36) == 36
assert sum_of_common_divisors(48, 48) == 48
assert sum_of_common_divisors(48, 60) == 48
assert sum_of_common