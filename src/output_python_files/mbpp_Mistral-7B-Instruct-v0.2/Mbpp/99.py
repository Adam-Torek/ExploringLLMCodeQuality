"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""
def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary += str(decimal % 2)
        decimal //= 2
    return binary[::-1]

assert decimal_to_binary(8) == '1000'
assert decimal_to_binary(15) == '1111'
assert decimal_to_binary(0) == ''
assert decimal_to_binary(1) == '1'
assert decimal_to_binary(10) == '1010'