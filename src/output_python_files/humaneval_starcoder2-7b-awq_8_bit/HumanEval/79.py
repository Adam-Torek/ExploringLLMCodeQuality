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
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be '0' to '9' or 'a' to 'f'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_hex("db1111db")   # returns "dbffdb"
    binary_to_hex("db100000db") # returns "db00db"
    """

def hex_to_binary(hex):
    """You will be given a number in hexadecimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    hex_to_binary("dbffdb")   # returns "db1111111111db"
    hex_to_binary("db00db")   # returns "db0000000000db"
    """

def hex_to_decimal(hex):
    """You will be given a number in hexadecimal form and your task is to convert it to
    decimal format. The function should return an integer.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    hex_to_decimal("dbffdb")   # returns 65535
    hex_to_decimal("db00db")   # returns 0
    """

def decimal_to_hex(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be '0' to '9' or 'a' to 'f'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hex(15)   # returns "dbffdb"
    decimal_to_hex(32)   # returns "db00db"
    """

def binary_to_hex_and_back(binary):
    """You will be given a number in binary form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be '0' to '9' or 'a' to 'f'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_hex_and_back("db1111db")   # returns "dbffdb"
    binary_to_hex_and_back("db100000db") # returns "db00db"