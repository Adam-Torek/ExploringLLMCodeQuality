def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    binary = bin(decimal)[2:]
    return f"db{binary.zfill(8)}db"



def binary_to_decimal(binary):
    """You will be given a binary string and your task is to convert it to decimal format.
    The function should return an integer.

    Examples:
    binary_to_decimal("1111")   # returns 15
    binary_to_decimal("100000")   # returns 32
    """
    return int(binary[2:-2], 2)



def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal form and your task is to convert it to hexadecimal format.
    The function should return a string, with each character representing a hexadecimal digit.

    There will be an extra character 'h' at the beginning and at the end of the string.
    The extra character is there to help with the format.

    Examples:
    decimal_to_hexadecimal(255)   # returns "hffh"
    decimal_to_hexadecimal(32)   # returns "h20h"
    """
    hexadecimal = hex(decimal)[2:]
    return f"h{hexadecimal}h"



def hexadecimal_to_decimal(hexadecimal):
    """You will be given a hexadecimal string and your task is to convert it to decimal format.
    The function should return an integer.

    Examples:
    hexadecimal_to_decimal("ff")   # returns 255
    hexadecimal_to_decimal("20")   # returns 32
    """
    return int(hexadecimal[1:-1], 16)



def decimal_to_octal(decimal):
    """You will be given a number in decimal form and your task is to convert it to octal format.
    The function should return a string, with each character representing an octal digit.

    There will be an extra character 'o' at the beginning and at the end of the string.
    The extra character is there to help with the format.

    Examples:
    decimal_to_octal(255)   # returns "o377o"
    decimal_to_octal(32)   # returns "o40o"
    """
    octal = oct(decimal)[2:]
    return f"o{octal}o"



def octal_to_decimal(octal):
    """You will be given an octal string and your task is to convert it to decimal format.
    The function should return an integer.

    Examples:
    octal_to_decimal