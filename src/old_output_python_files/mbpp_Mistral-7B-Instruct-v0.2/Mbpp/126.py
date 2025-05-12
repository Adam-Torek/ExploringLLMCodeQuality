"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""
from math import gcd

def sum_of_common_divisors(num1, num2):
    """
    Function to find the sum of common divisors of two given numbers.
    :param num1: First number
    :param num2: Second number
    :return: Sum of common divisors
    """
    common_divisors = set()
    i = 1
    while i <= min(num1, num2):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.add(i)
        i += 1
    return sum(common_divisors)

assert sum_of_common_divisors(10, 15) == 6
assert sum_of_common_divisors(12, 18) == 12
assert sum_of_common_divisors(17, 23) == 1
assert sum_of_common_divisors(2, 4) == 2
assert sum_of_common_divisors(15, 21) == 3
assert sum_of_common_divisors(1, 1) == 1
assert sum_of_common_divisors(1, 2) == 1
assert sum_of_common_divisors(1, 3) == 0
assert sum_of_common_divisors(1, 4) == 1
assert sum_of_common_divisors(1, 5) == 0
assert sum_of_common_divisors(1, 6) == 1
assert sum_of_common_divisors(1, 7) == 0
assert sum_of_common_divisors(1, 8) == 1
assert sum_of_common_divisors(1, 9) == 1
assert sum_of_common_divisors(1, 10) == 1
assert sum_of_common_divisors(1, 11) == 0
assert sum_of_common_divisors(1, 12) == 1
assert sum_of_common_divisors(1, 13) == 0
assert sum_of_common_divisors(1, 14) == 1
assert sum_of_common_divisors(1, 15) == 1
assert sum_of_common_divisors(1, 16) == 1
assert sum_of_common_divisors(1, 17) == 0
assert sum_of_common_divisors(1, 18) == 1
assert sum_of_common_divisors(1, 19) == 0
assert sum_of_common_divisors(1, 20) == 1
assert sum_of_common_divisors(1, 21) == 0
assert sum_of_common_divisors(1, 22) == 1
assert sum_of_common_divisors(1, 23) == 0
assert sum_of_common_divisors(1, 24) == 1
assert sum_of_common_divisors(1, 25) == 1
assert sum_of_common_divisors(1, 26) == 1
assert sum_of_common_divisors(1, 27) == 0
assert sum_of_common_divisors(1, 28) == 1
assert sum_of_common_divisors(1, 29) == 0
assert sum_of_common_divisors(1, 30) == 1
assert sum_of_common_divisors(1, 31) == 0
assert sum_of_common_divisors(1, 32) == 1
assert sum_of_common_divisors(1, 33) == 0
assert sum_of_common_divisors(1, 34) == 1
assert sum_of_common_divisors(1, 35) == 1