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

def binary_to_decimal(binary):
    """You will be given a number in binary form and your task is to convert it to
    decimal format. The function should return an integer.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db") # returns 32
    """

def binary_to_hex(binary):
    """You will be given a number in binary form and your task is to convert it to
    hexadecimal format. The function should return a string.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_hex("db1111db")   # returns "dbffdb"
    binary_to_hex("db100000db") # returns "db80db"
    """

def hex_to_binary(hex):
    """You will be given a number in hexadecimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    hex_to_binary("dbffdb")   # returns "db1111111111db"
    hex_to_binary("db80db")   # returns "db100000000db"
    """

def binary_to_hex_and_back(binary):
    """You will be given a number in binary form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_hex_and_back("db1111111111db")   # returns "dbffdb"
    binary_to_hex_and_back("db100000000db")   # returns "db80db"
    """

def hex_to_binary_and_back(hex):
    """You will be given a number in hexadecimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    hex_to_binary_and_back("dbffdb")   # returns "db1111