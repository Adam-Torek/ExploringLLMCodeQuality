"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""

def sum_common_divisors(num1, num2):
    divisors = []
    for i in range(1, num1+1):
        if num1 % i == 0 and num2 % i == 0:
            divisors.append(i)
    return sum(divisors)

assert sum_common_divisors(10, 15) == 6<|endoftext|>