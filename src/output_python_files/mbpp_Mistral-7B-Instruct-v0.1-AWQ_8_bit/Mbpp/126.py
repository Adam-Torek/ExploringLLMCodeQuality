"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""

def sum_of_common_divisors(a, b):
    """
    This function takes two numbers as input and returns the sum of their common divisors.
    """
    # Finding the greatest common divisor of two numbers
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Finding the sum of common divisors
    result = 0
    for i in range(1, gcd(a, b)+1):
        if a % i == 0 and b % i == 0:
            result += i
    return result

# Testing the function
assert sum_of_common_divisors(10, 15) == 6