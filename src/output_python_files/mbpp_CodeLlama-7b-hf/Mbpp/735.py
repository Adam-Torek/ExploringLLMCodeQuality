"""
Write a python function to toggle bits of the number except the first and the last bit. https://www.geeksforgeeks.org/toggle-bits-number-expect-first-last-bits/
assert toggle_middle_bits(9) == 15
"""


def toggle_middle_bits(n):
    """
    Toggle all bits except the first and the last bit.
    :param n: number
    :return: number
    """
    return (n ^ (n >> 1) ^ (n >> 2)) & 0x7fffffff


if __name__ == '__main__':
    print(toggle_middle_bits(9))
    print(toggle_middle_bits(10))
    print(toggle_middle_bits(11))
    print(toggle_middle_bits(12))
    print(toggle_middle_bits(13))
    print(toggle_middle_bits(14))
    print(toggle_middle_bits(15))
    print(toggle_middle_bits(16))
    print(toggle_middle_bits(17))
    print(toggle_middle_bits(18))
    print(toggle_middle_bits(19))
    print(toggle_middle_bits(20))
    print(toggle_middle_bits(21))
    print(toggle_middle_bits(22))
    print(toggle_middle_bits(23))
    print(toggle_middle_bits(24))
    print(toggle_middle_bits(25))
    print(toggle_middle_bits(26))
    print(toggle_middle_bits(27))
    print(toggle_middle_bits(28))
    print(toggle_middle_bits(29))
    print(toggle_middle_bits(30))
    print(toggle_middle_bits(31))
    print(toggle_middle_bits(32))
    print(toggle_middle_bits(33))
    print(toggle_middle_bits(34))
    print(toggle_middle_bits(35))
    print(toggle_middle_bits(36))
    print(toggle_middle_bits(37))
    print(toggle_middle_bits(38))
    print(toggle_middle_bits(39))
    print(toggle_middle_bits(40))
    print(toggle_middle_bits(41))
    print(toggle_middle_bits(42))
    print(toggle_middle_bits(43))
    print(toggle_middle_bits(44))
    print(toggle_middle_bits(45))
    print(toggle_middle_bits(46))
    print(toggle_middle_bits(47))
    print(toggle_middle_bits(48))
    print(toggle_middle_bits(49))
    print(toggle_middle_bits(50))
    print(toggle_middle_bits(51))
    print(toggle_middle_bits(52))
    print(toggle_middle_bits(53))
    print(toggle_middle_bits(54))
    print(toggle_middle_bits(55))
    print(toggle_middle_bits(56))
    print(toggle_middle_bits(57))
    print(toggle_middle_bits(58))
    print(toggle_middle_bits(59))
    print(toggle_middle_bits(60))
    print(toggle_middle_bits(61))
    print(toggle_middle_bits(62))
    print(toggle_middle_bits(63))
    print(toggle_middle_bits(64))
    print(toggle_middle_bits(65))
    print(toggle_middle_bits(66))
    print(toggle_middle_bits(67))
    print(toggle_middle_bits(68))
    print(toggle_middle_bits(69))
    print(toggle_middle_bits(70))
    print(toggle_middle_bits(71))
    print(toggle_middle_bits(72))
    print(toggle_middle_bits(73))
    print(toggle_middle_bits(74))
    print(toggle_middle_bits