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
    # Your code here
    return "db" + bin(decimal)[2:] + "db"


def binary_to_decimal(binary):
    """You will be given a string in binary format and your task is to convert it to decimal form.
    The function should return an integer.

    There will be an extra couple of characters 'bd' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db") # returns 32
    """
    # Your code here
    return int("".join(binary[2:-2]), 2)


def binary_to_hexadecimal(binary):
    """You will be given a string in binary format and your task is to convert it to hexadecimal form.
    The function should return a string.

    There will be an extra couple of characters 'bh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_hexadecimal("db000000db")   # returns "bh0db"
    binary_to_hexadecimal("db000010db")   # returns "bh2db"
    binary_to_hexadecimal("db000011db")   # returns "bh3db"
    binary_to_hexadecimal("db000100db")   # returns "bh4db"
    binary_to_hexadecimal("db000101db")   # returns "bh5db"
    binary_to_hexadecimal("db000110db")   # returns "bh6db"
    binary_to_hexadecimal("db000111db")   # returns "bh7db"
    binary_to_hexadecimal("db001000db")   # returns "bh8db"
    binary_to_hexadecimal("db001001db")   # returns "bh9db"
    binary_to_hexadecimal("db001010db")   # returns "bha0db"
    binary_to_hexadecimal("db001011db")   # returns "bha1db"
    binary_to_hexadecimal("db001100db")   # returns "bha2db"
    binary_to_hexadecimal("db001101db")   # returns "bha3db"
    binary_to_hexadecimal("db001110db")   # returns "bha4db"
    binary_to_hexadecimal("db001111db")   # returns "bha5db"
    binary_to_hexadecimal("db010000db")   # returns "bha6db"
    binary_to_hexadecimal("db010001db")   # returns "bha7db"
    binary_to_hexadecimal("db010010db")   # returns "bhc0db"
    binary_to_hexadecimal("db010011db")   # returns "bhc1db"
    binary_to_hexadecimal("db010100db")   # returns "bhc2db"