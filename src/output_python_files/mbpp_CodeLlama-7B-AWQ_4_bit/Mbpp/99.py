"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""


def decimal_to_binary(decimal_number):
    """
    :param decimal_number: int
    :return: str
    """
    binary_number = ''
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number //= 2
    return binary_number


if __name__ == '__main__':
    print(decimal_to_binary(8))
    print(decimal_to_binary(10))
    print(decimal_to_binary(11))
    print(decimal_to_binary(12))
    print(decimal_to_binary(13))
    print(decimal_to_binary(14))
    print(decimal_to_binary(15))
    print(decimal_to_binary(16))
    print(decimal_to_binary(17))
    print(decimal_to_binary(18))
    print(decimal_to_binary(19))
    print(decimal_to_binary(20))
    print(decimal_to_binary(21))
    print(decimal_to_binary(22))
    print(decimal_to_binary(23))
    print(decimal_to_binary(24))
    print(decimal_to_binary(25))
    print(decimal_to_binary(26))
    print(decimal_to_binary(27))
    print(decimal_to_binary(28))
    print(decimal_to_binary(29))
    print(decimal_to_binary(30))
    print(decimal_to_binary(31))
    print(decimal_to_binary(32))
    print(decimal_to_binary(33))
    print(decimal_to_binary(34))
    print(decimal_to_binary(35))
    print(decimal_to_binary(36))
    print(decimal_to_binary(37))
    print(decimal_to_binary(38))
    print(decimal_to_binary(39))
    print(decimal_to_binary(40))
    print(decimal_to_binary(41))
    print(decimal_to_binary(42))
    print(decimal_to_binary(43))
    print(decimal_to_binary(44))
    print(decimal_to_binary(45))
    print(decimal_to_binary(46))
    print(decimal_to_binary(47))
    print(decimal_to_binary(48))
    print(decimal_to_binary(49))
    print(decimal_to_binary(50))
    print(decimal_to_binary(51))
    print(decimal_to_binary(52))
    print(decimal_to_binary(53))
    print(decimal_to_binary(54))
    print(decimal_to_binary(55))
    print(decimal_to_binary(56))
    print(decimal_to_binary(57))
    print(decimal_to_binary(58))
    print(decimal_to_binary(59))
    print(decimal_to_binary(60))
    print(decimal_to_binary(61))
    print(decimal_to_binary(62))
    print(decimal_to_binary(63))
    print(decimal_to_binary(64))
    print(decimal_to_binary(65))
    print(decimal_to_binary(66))
    print(decimal_to_binary(67))
    print(decimal_to_binary(68))
    print(decimal_to_binary(69))