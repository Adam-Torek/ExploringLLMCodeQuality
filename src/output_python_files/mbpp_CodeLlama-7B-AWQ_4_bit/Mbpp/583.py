"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""


def catalan_number(n):
    """
    :param n: int
    :return: int
    """
    if n == 0:
        return 1
    else:
        return (2 * n - 1) * catalan_number(n - 1) / n


if __name__ == '__main__':
    print(catalan_number(10))
    print(catalan_number(11))
    print(catalan_number(12))
    print(catalan_number(13))
    print(catalan_number(14))
    print(catalan_number(15))
    print(catalan_number(16))
    print(catalan_number(17))
    print(catalan_number(18))
    print(catalan_number(19))
    print(catalan_number(20))
    print(catalan_number(21))
    print(catalan_number(22))
    print(catalan_number(23))
    print(catalan_number(24))
    print(catalan_number(25))
    print(catalan_number(26))
    print(catalan_number(27))
    print(catalan_number(28))
    print(catalan_number(29))
    print(catalan_number(30))
    print(catalan_number(31))
    print(catalan_number(32))
    print(catalan_number(33))
    print(catalan_number(34))
    print(catalan_number(35))
    print(catalan_number(36))
    print(catalan_number(37))
    print(catalan_number(38))
    print(catalan_number(39))
    print(catalan_number(40))
    print(catalan_number(41))
    print(catalan_number(42))
    print(catalan_number(43))
    print(catalan_number(44))
    print(catalan_number(45))
    print(catalan_number(46))
    print(catalan_number(47))
    print(catalan_number(48))
    print(catalan_number(49))
    print(catalan_number(50))
    print(catalan_number(51))
    print(catalan_number(52))
    print(catalan_number(53))
    print(catalan_number(54))
    print(catalan_number(55))
    print(catalan_number(56))
    print(catalan_number(57))
    print(catalan_number(58))
    print(catalan_number(59))
    print(catalan_number(60))
    print(catalan_number(61))
    print(catalan_number(62))
    print(catalan_number(63))
    print(catalan_number(64))
    print(catalan_number(65))
    print(catalan_number(66))
    print(catalan_number(67))
    print(catalan_number(68))
    print(catalan_number(69))
    print(catalan_number(70))
    print(catalan_number(71))
    print(catalan_number(72))
    print(catalan_number(73))
    print(catalan_number(74))
    print(catalan_number(75))
    print(catalan_number(76))
    print(catalan_number(77))
    print(catalan_number(78))
    print(catalan_number(79))
    print(catalan_number(80))
    print(catalan_number(81))
    print(catalan_number