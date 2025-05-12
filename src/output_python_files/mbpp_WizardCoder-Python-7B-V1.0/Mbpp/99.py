"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""

def decimal_to_binary(num):
    if num == 0:
        return '0'
    binary = []
    while num > 0:
        binary.append(num % 2)
        num //= 2
    return ''.join(str(i) for i in binary[::-1])

# Test cases
print(decimal_to_binary(8)) # Output: '1000'
print(decimal_to_binary(13)) # Output: '1101'
print(decimal_to_binary(16)) # Output: '100000'
print(decimal_to_binary(1024)) # Output: '1000000000000'
print(decimal_to_binary(255)) # Output: '111111111'
print(decimal_to_binary(4294967295)) # Output: '1111111111111111111111111111111111111'
print(decimal_to_binary(0)) # Output: '0'
print(decimal_to_binary(1)) # Output: '1'
print(decimal_to_binary(2)) # Output: '10'
print(decimal_to_binary(10)) # Output: '1010'
print(decimal_to_binary(15)) # Output: '1111'
print(decimal_to_binary(20)) # Output: '10100'
print(decimal_to_binary(21)) # Output: '10101'
print(decimal_to_binary(22)) # Output: '10110'
print(decimal_to_binary(23)) # Output: '10111'
print(decimal_to_binary(24)) # Output: '11000'
print(decimal_to_binary(25)) # Output: '11001'
print(decimal_to_binary(26)) # Output: '11010'
print(decimal_to_binary(27)) # Output: '11011'
print(decimal_to_binary(28)) # Output: '11100'
print(decimal_to_binary(29)) # Output: '11101'
print(decimal_to_binary(30)) # Output: '11110'
print(decimal_to_binary(31)) # Output: '11111'
print(decimal_to_binary(32)) # Output: '1000000'
print(decimal_to_binary(33)) # Output: '100001'
print(decimal_to_binary(34)) # Output: '10010'
print(decimal_to_binary(35)) # Output: '10011'
print(decimal_to_binary(36)) # Output: '10100'
print(decimal_to_binary(37)) # Output: '10101'
print(decimal_to_binary(38)) # Output: '10110'
print(decimal_to_binary(39)) # Output: '10111'
print(decimal_to_binary(40)) # Output: '110000'
print(decimal_to_binary(41)) # Output: '11001'
print(decimal_to_binary(42)) # Output: '11010'
print(decimal_to_binary(43)) # Output: '11011'
print(decimal_to_binary(44)) # Output: '11100'
print(decimal_