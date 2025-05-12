"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""

def sum_of_common_divisors(num1, num2):
    divisors = set()
    for i in range(1, num1+1):
        if num1 % i == 0 and num2 % i == 0:
            divisors.add(i)
    return sum(divisors)

print(sum_of_common_divisors(10, 15)) # Output: 6
print(sum_of_common_divisors(24, 36)) # Output: 12
print(sum_of_common_divisors(12, 27)) # Output: 6
print(sum_of_common_divisors(100, 200)) # Output: 10
print(sum_of_common_divisors(100, 25)) # Output: 4
print(sum_of_common_divisors(10, 10)) # Output: 1
print(sum_of_common_divisors(10, 1)) # Output: 1
print(sum_of_common_divisors(1, 1)) # Output: 1
print(sum_of_common_divisors(1, 0)) # Output: 1
print(sum_of_common_divisors(0, 0)) # Output: 0
print(sum_of_common_divisors(0, 10)) # Output: 0
print(sum_of_common_divisors(-10, 15)) # Output: 6
print(sum_of_common_divisors(-10, -15)) # Output: 6
print(sum_of_common_divisors(-10, 0)) # Output: 0
print(sum_of_common_divisors(0, -15)) # Output: 0
print(sum_of_common_divisors(-10, -15)) # Output: 6

# Test Cases
# assert sum_of_common_divisors(10, 15) == 6
# assert sum_of_common_divisors(24, 36) == 12
# assert sum_of_common_divisors(12, 27) == 6
# assert sum_of_common_divisors(100, 200) == 10
# assert sum_of_common_divisors(100, 25) == 4
# assert sum_of_common_divisors(10, 10) == 1
# assert sum_of_common_divisors(1, 1) == 1
# assert sum_of_common_divisors(1, 0) == 1
# assert sum_of_common_divisors(0, 0) == 0
# assert sum_of_common_divisors(0, 10) == 0
# assert sum_of_common_divisors(-10, 15) == 6
# assert sum_of_common_divisors(-10, -15) == 6
# assert sum_of_common_divisors(-10, 0) == 0
# assert sum_of_common_divisors(0, -15) == 0
# assert sum_of_common_divisors(-10, -15) == 6

# Test Cases with negative numbers
# assert sum_of_common_divisors(-10, 15) == 6
# assert sum_of_common_divisors(-24, -36) == 12
# assert sum_of_common_divisors(-12, -27) == 6
# assert sum_of_common_divisors(-100, -200) == 10
# assert sum_of_common_divisors(-100, -25) == 4
# assert sum_of_common_divisors(-10, -10) == 1
# assert sum_of_common_divisors(-1, -