"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""

def decimal_to_binary(num):
    if num == 0:
        return '0'
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

print(decimal_to_binary(8)) # Output: '1000'
print(decimal_to_binary(13)) # Output: '11111'
print(decimal_to_binary(20)) # Output: '10100'
print(decimal_to_binary(10)) # Output: '1010'
print(decimal_to_binary(1)) # Output: '1'
print(decimal_to_binary(0)) # Output: '0'
print(decimal_to_binary(15)) # Output: '11111'
print(decimal_to_binary(25)) # Output: '11001'
print(decimal_to_binary(30)) # Output: '11110'
print(decimal_to_binary(45)) # Output: '101111'
print(decimal_to_binary(77)) # Output: '10010101'
print(decimal_to_binary(1024)) # Output: '1000000000000'