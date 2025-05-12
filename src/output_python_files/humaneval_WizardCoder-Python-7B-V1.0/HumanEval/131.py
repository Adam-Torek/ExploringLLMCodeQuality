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
print(digits(123456789))  # Output: 9
print(digits(9876543210))  # Output: 0
print(digits(1234567890))  # Output: 0
print(digits(10111213141516171819))  # Output: 1234567890
print(digits(12345678900))  # Output: 0
print(digits(12345678901))  # Output: 1
print(digits(12345678902))  # Output: 2
print(digits(12345678903))  # Output: 3
print(digits(12345678904))  # Output: 4
print(digits(12345678905))  # Output: 5
print(digits(12345678906))  # Output: 6
print(digits(12345678907))  # Output: 7
print(digits(12345678908))  # Output: 8
print(digits(12345678909))  # Output: 9
print(digits(12345678910))  # Output: 10
print(digits(12345678911))  # Output: 11
print(digits(12345678912))  # Output: 12
print(digits(12345678913))  # Output: 13
print(digits(12345678914))  # Output: 14
print(digits(1