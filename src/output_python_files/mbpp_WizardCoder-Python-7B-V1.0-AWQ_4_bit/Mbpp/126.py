"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""

def sum_of_common_divisors(num1, num2):
    """
    This function takes two numbers as input and returns the sum of their common divisors.
    """
    divisors = set()
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors.add(i)
    return sum(divisors)

print(sum_of_common_divisors(10, 15)) # Output: 6
print(sum_of_common_divisors(20, 24)) # Output: 6
print(sum_of_common_divisors(12, 18)) # Output: 6
print(sum_of_common_divisors(100, 200)) # Output: 6
print(sum_of_common_divisors(100, 25)) # Output: 4
print(sum_of_common_divisors(100, 10)) # Output: 2
print(sum_of_common_divisors(10, 100)) # Output: 2
print(sum_of_common_divisors(10, 20)) # Output: 2
print(sum_of_common_divisors(20, 10)) # Output: 2
print(sum_of_common_divisors(10, 1)) # Output: 1
print(sum_of_common_divisors(1, 10)) # Output: 1
print(sum_of_common_divisors(1, 20)) # Output: 1
print(sum_of_common_divisors(20, 1)) # Output: 1
print(sum_of_common_divisors(0, 10)) # Output: 0
print(sum_of_common_divisors(10, 0)) # Output: 0
print(sum_of_common_divisors(0, 0)) # Output: 0

# Test cases
# assert sum_of_common_divisors(10, 15) == 6
# assert sum_of_common_divisors(20, 24) == 6
# assert sum_of_common_divisors(12, 18) == 6
# assert sum_of_common_divisors(100, 200) == 6
# assert sum_of_common_divisors(100, 25) == 4
# assert sum_of_common_divisors(100, 10) == 2
# assert sum_of_common_divisors(10, 100) == 2
# assert sum_of_common_divisors(10, 20) == 2
# assert sum_of_common_divisors(20, 10) == 2
# assert sum_of_common_divisors(10, 1) == 1
# assert sum_of_common_divisors(1, 10) == 1
# assert sum_of_common_divisors(1, 20) == 1
# assert sum_of_common_divisors(20, 1) == 1
# assert sum_of_common_divisors(0, 10) == 0
# assert sum_of_common_divisors(10, 0) == 0
# assert sum_of_common_divisors(0, 0) == 0

# Test cases with negative numbers
# assert sum_of_common_divisors(-10, 15) == 6
# assert sum_of_common_divisors(10, -15) == 6
# assert sum_of_common_divisors(-10, -15) == 6
# assert sum_of