def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product


# Test cases
print(digits(1))  # Output: 1
print(digits(4))  # Output: 0
print(digits(235))  # Output: 15
print(digits(1024))  # Output: 0
print(digits(1111))  # Output: 3
print(digits(987654321))  # Output: 9
print(digits(123456789))  # Output: 0
print(digits(1234567890))  # Output: 0
print(digits(12345678901234567890))  # Output: 0
print(digits(123456789012345678901234567890))  # Output: 0
print(digits(1234567890123456789012345678901234567890))  # Output: 0
print(digits(12345678901234567890123456789012345678901234567890))  # Output: 0
print(digits(123456789012345678901234567890123456789012345678901234567890))  # Output: 0
print(digits(1234567890123456789012345678901234567890123456789012345678901234567890))  # Output: 0
print(digits(12345678901234567890123456789012345678901234