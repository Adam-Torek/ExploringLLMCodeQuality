"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""


def find_lucas(n):
    """
    Find the n'th lucas number.
    :param n: int
    :return: int
    """
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return find_lucas(n - 1) + find_lucas(n - 2)


if __name__ == '__main__':
    print(find_lucas(9))
    print(find_lucas(10))
    print(find_lucas(11))
    print(find_lucas(12))
    print(find_lucas(13))
    print(find_lucas(14))
    print(find_lucas(15))
    print(find_lucas(16))
    print(find_lucas(17))
    print(find_lucas(18))
    print(find_lucas(19))
    print(find_lucas(20))
    print(find_lucas(21))
    print(find_lucas(22))
    print(find_lucas(23))
    print(find_lucas(24))
    print(find_lucas(25))
    print(find_lucas(26))
    print(find_lucas(27))
    print(find_lucas(28))
    print(find_lucas(29))
    print(find_lucas(30))
    print(find_lucas(31))
    print(find_lucas(32))
    print(find_lucas(33))
    print(find_lucas(34))
    print(find_lucas(35))
    print(find_lucas(36))
    print(find_lucas(37))
    print(find_lucas(38))
    print(find_lucas(39))
    print(find_lucas(40))
    print(find_lucas(41))
    print(find_lucas(42))
    print(find_lucas(43))
    print(find_lucas(44))
    print(find_lucas(45))
    print(find_lucas(46))
    print(find_lucas(47))
    print(find_lucas(48))
    print(find_lucas(49))
    print(find_lucas(50))
    print(find_lucas(51))
    print(find_lucas(52))
    print(find_lucas(53))
    print(find_lucas(54))
    print(find_lucas(55))
    print(find_lucas(56))
    print(find_lucas(57))
    print(find_lucas(58))
    print(find_lucas(59))
    print(find_lucas(60))
    print(find_lucas(61))
    print(find_lucas(62))
    print(find_lucas(63))
    print(find_lucas(64))
    print(find_lucas(65))
    print(find_lucas(66))
    print(find_lucas(67))
    print(find_lucas(68))
    print(find_lucas(69))
    print(find_lucas(70))
    print(find_lucas(71))
    print(find_lucas(72))
    print(find_lucas(73))
    print(find_lucas(74))
    print(find_lucas(75))
    print(find_lucas(