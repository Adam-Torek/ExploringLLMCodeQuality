"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""

def decimal_to_binary(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

# Test cases
assert decimal_to_binary(8) == '1000'
assert decimal_to_binary(15) == '1111'
assert decimal_to_binary(0) == '0'
assert decimal_to_binary(1) == '1'<|endoftext|>