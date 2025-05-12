"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""

def sum_digits(n):
    """
    Returns the sum of the digits of a non-negative integer.
    """
    if n < 0:
        return None
    else:
        return sum(int(digit) for digit in str(n))

print(sum_digits(345)) # Output: 8
print(sum_digits(12345)) # Output: 12
print(sum_digits(0)) # Output: 0
print(sum_digits(-345)) # Output: None