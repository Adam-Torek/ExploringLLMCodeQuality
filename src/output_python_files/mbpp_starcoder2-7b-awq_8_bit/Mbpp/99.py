"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""

def decimal_to_binary(n):
    """
    :param n: int
    :return: str
    """
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result

def test_decimal_to_binary():
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(10) == '1010'
    assert decimal_to_binary(0) == '0'
    assert decimal_to_binary(1) == '1'
    assert decimal_to_binary(2) == '10'
    assert decimal_to_binary(3) == '11'
    assert decimal_to_binary(4) == '100'
    assert decimal_to_binary(5) == '101'
    assert decimal_to_binary(6) == '110'
    assert decimal_to_binary(7) == '111'
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(9) == '1001'
    assert decimal_to_binary(10) == '1010'
    assert decimal_to_binary(11) == '1011'
    assert decimal_to_binary(12) == '1100'
    assert decimal_to_binary(13) == '1101'
    assert decimal_to_binary(14) == '1110'
    assert decimal_to_binary(15) == '1111'
    assert decimal_to_binary(16) == '10000'
    assert decimal_to_binary(17) == '10001'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(19) == '10011'
    assert decimal_to_binary(20) == '10100'
    assert decimal_to_binary(21) == '10101'
    assert decimal_to_binary(22) == '10110'
    assert decimal_to_binary(23) == '10111'
    assert decimal_to_binary(24) == '11000'
    assert decimal_to_binary(25) == '11001'
    assert decimal_to_binary(26) == '11010'
    assert decimal_to_binary(27) == '11011'
    assert decimal_to_binary(28) == '11100'
    assert decimal_to_binary(29) == '11101'
    assert decimal_to_binary(30) == '11110'
    assert decimal_to_binary(31) == '11111'
    assert decimal_to_binary(32) == '100000'
    assert decimal_to_binary(33) == '100001'
    assert decimal_to_binary(34) == '100010'
    assert decimal_to_binary(35) == '100011'
    assert decimal_to_binary(36) == '100100'
    assert decimal_to_binary(37) == '100101'
    assert decimal_to_binary(38) == '100110'
    assert decimal_to_binary(39) == '100111'
    assert decimal_to_binary(40) == '101000'
    assert decimal_to_binary(41) == '101001'
    assert decimal_to_binary(42) == '101010'
    assert decimal_to_binary(43) == '101011'
    assert decimal_to_binary(44) == '101100'
    assert decimal_to_binary(45) == '101101'
    assert decimal_to_binary(46) == '10