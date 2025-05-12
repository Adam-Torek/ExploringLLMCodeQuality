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
    return f"db{binary}db"



def binary_to_decimal(binary):
    """You will be given a binary string and your task is to convert it to decimal format.
    The function should return an integer.

    Examples:
    binary_to_decimal("1111")   # returns 7
    binary_to_decimal("100000")   # returns 16
    """
    return int(binary[2:-2], 2)



def decimal_to_hexadecimal(decimal):
    """You will be given a decimal number and your task is to convert it to hexadecimal format.
    The function should return a string, with each character representing a hexadecimal digit.

    Examples:
    decimal_to_hexadecimal(15)   # returns "db0fdb"
    decimal_to_hexadecimal(32)   # returns "db10db"
    """
    return hex(decimal)[2:]



def hexadecimal_to_decimal(hexadecimal):
    """You will be given a hexadecimal string and your task is to convert it to decimal format.
    The function should return an integer.

    Examples:
    hexadecimal_to_decimal("1f")   # returns 31
    hexadecimal_to_decimal("10")   # returns 16
    """
    return int(hexadecimal, 16)



def hexadecimal_to_binary(hexadecimal):
    """You will be given a hexadecimal string and your task is to convert it to binary format.
    The function should return a string, with each character representing a binary number.

    Examples:
    hexadecimal_to_binary("1f")   # returns "db11111db"
    hexadecimal_to_binary("10")   # returns "db1010db"
    """
    return bin(int(hexadecimal, 16))[2:]



def binary_to_hexadecimal(binary):
    """You will be given a binary string and your task is to convert it to hexadecimal format.
    The function should return a string, with each character representing a hexadecimal digit.

    Examples:
    binary_to_hexadecimal("1111")   # returns "db0fdb"
    binary_to_hexadecimal("1010")   # returns "db10db"
    """
    return hex(int(binary[2:-2], 2))[2:]



def main():
    decimal = 15
    print(f"Decimal