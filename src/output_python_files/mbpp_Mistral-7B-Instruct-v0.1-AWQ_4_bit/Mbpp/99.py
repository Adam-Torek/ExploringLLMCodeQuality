"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""
def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

# Test the function
assert decimal_to_binary(8) == '1000'
assert decimal_to_binary(10) == '1010'
assert decimal_to_binary(15) == '1111'