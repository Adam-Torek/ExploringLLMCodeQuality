from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result

def string_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary AND on these inputs and return result also as a string.
    >>> string_and('010', '110')
    '010'
    """
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '1'
        else:
            result += '0'
    return result

def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary OR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '111'
    """
    result = ''
    for i in range(len(a)):
        if a[i] == '1' or b[i] == '1':
            result += '1'
        else:
            result += '0'
    return result

def string_not(a: str) -> str:
    """ Input is a string consisting only of 1s and 0s.
    Perform binary NOT on this input and return result also as a string.
    >>> string_not('010')
    '101'
    """
    result = ''
    for i in range(len(a)):
        if a[i] == '0':
            result += '1'
        else:
            result += '0'
    return result

def binary_to_decimal(binary: str) -> int:
    """ Input is a string consisting only of 1s and 0s.
    Convert this binary number to decimal and return the result as an integer.
    >>> binary_to_decimal('1010')
    10
    """
    decimal = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2**(len(binary)-1-i)
    return decimal

def decimal_to_binary(decimal: int, num_bits: int) -> str:
    """ Input is an integer and the number of bits to use for the binary representation.
    Convert this decimal number to binary and return the result as a string.
    >>> decimal_to_binary(10, 4)
    '1010'
    """
    binary = ''
    for i in range(num_bits):
        if decimal % 2 == 1:
            binary += '1'
        else:
            binary += '0'
        decimal //= 2
    return binary[::-1]

def decimal_to_hex(decimal: int) -> str:
    """ Input is an integer.
    Convert this decimal number to hexadecimal and return the result as a string.
    >>> decimal_to_hex(10)
    'A'
    """
    hex_chars = '0123456789ABCDEF'
    hex_string = ''
    while decimal > 0:
        hex_string += hex_chars[decimal % 16]
        decimal //= 16
    return hex_string[::-1]

def hex