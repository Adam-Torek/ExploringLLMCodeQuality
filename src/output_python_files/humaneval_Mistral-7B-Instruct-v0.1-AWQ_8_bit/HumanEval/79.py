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
    # check if the number is negative
    if decimal < 0:
        decimal = -decimal
        # add a '1' to the beginning of the string
        result = 'db' + bin(decimal)[2:] + 'db'
    else:
        # add a '0' to the beginning of the string
        result = 'db' + bin(decimal)[2:] + 'db'
    return result

def binary_to_decimal(binary):
    """You will be given a string in binary format and your task is to convert it to
    decimal format. The function should return an integer.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db") # returns 32
    """
    # remove the extra characters 'db' from the beginning and at the end of the string
    binary = binary[2:-2]
    # convert the binary string to an integer
    decimal = int(binary, 2)
    return decimal