"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""


def decimal_to_binary(decimal_number):
    """
    :param decimal_number: int
    :return: str
    """
    if decimal_number == 0:
        return '0'
    binary_number = ''
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number


if __name__ == '__main__':
    print(decimal_to_binary(8))
    print(decimal_to_binary(10))
    print(decimal_to_binary(123456789))
    print(decimal_to_binary(1234567890))
    print(decimal_to_binary(12345678901))
    print(decimal_to_binary(123456789012))
    print(decimal_to_binary(1234567890123))
    print(decimal_to_binary(12345678901234))
    print(decimal_to_binary(123456789012345))
    print(decimal_to_binary(1234567890123456))
    print(decimal_to_binary(12345678901234567))
    print(decimal_to_binary(123456789012345678))
    print(decimal_to_binary(1234567890123456789))
    print(decimal_to_binary(12345678901234567890))
    print(decimal_to_binary(123456789012345678901))
    print(decimal_to_binary(1234567890123456789012))
    print(decimal_to_binary(12345678901234567890123))
    print(decimal_to_binary(123456789012345678901234))
    print(decimal_to_binary(1234567890123456789012345))
    print(decimal_to_binary(12345678901234567890123456))
    print(decimal_to_binary(123456789012345678901234567))
    print(decimal_to_binary(1234567890123456789012345678))
    print(decimal_to_binary(12345678901234567890123456789))
    print(decimal_to_binary(123456789012345678901234567890))
    print(decimal_to_binary(1234567890123456789012345678901))
    print(decimal_to_binary(12345678901234567890123456789012))
    print(decimal_to_binary(123456789012345678901234567890123))
    print(decimal