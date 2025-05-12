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
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = int(decimal / 2)
    return 'db' + binary + 'db'


def binary_to_decimal(binary):
    """You will be given a string in binary format and your task is to convert it to decimal form.
    The function should return an integer.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db")   # returns 32
    """
    binary = binary[2:-2]
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - i - 1))
    return decimal


def binary_to_decimal_2(binary):
    """You will be given a string in binary format and your task is to convert it to decimal form.
    The function should return an integer.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db")   # returns 32
    """
    binary = binary[2:-2]
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - i - 1))
    return decimal


def binary_to_decimal_3(binary):
    """You will be given a string in binary format and your task is to convert it to decimal form.
    The function should return an integer.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db")   # returns 32
    """
    binary = binary[2:-2]
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - i - 1))
    return decimal


def binary_to_decimal_4(binary):
    """You will be given a string in binary format and your task is to convert it to