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
    binary_to_decimal("db100000db")   # returns 32
    """
    # Your code here
    return int(binary[2:-2], 2)


def binary_to_hex(binary):
    """You will be given a string in binary format and your task is to convert it to hexadecimal form.
    The function should return a string.

    There will be an extra couple of characters 'bh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_hex("bh1111001101001100011db")   # returns "bh333c5db"
    binary_to_hex("bh1111001101001100011db")   # returns "bh333c5db"
    """
    # Your code here
    return "bh" + hex(int(binary[2:-2], 2))[2:] + "db"


def hex_to_binary(hexadecimal):
    """You will be given a string in hexadecimal format and your task is to convert it to binary form.
    The function should return a string.

    There will be an extra couple of characters 'hb' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    hex_to_binary("hb333c5db")   # returns "hb1111001101001100011db"
    hex_to_binary("hb333c5db")   # returns "hb1111001101001100011db"
    """
    # Your code here
    return "hb" + bin(int(hexadecimal[2:-2], 16))[2:] + "db"


def binary_to_octal(binary):
    """You will be given a string in binary format and your task is to convert it to octal form.
    The function should return a string.