"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_digits(n//10)

print(sum_digits(345)) # Output: 9
print(sum_digits(123)) # Output: 6
print(sum_digits(9876543210)) # Output: 45
print(sum_digits(123000)) # Output: 6
print(sum_digits(0)) # Output: 0