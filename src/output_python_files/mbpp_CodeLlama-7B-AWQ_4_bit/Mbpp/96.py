"""
Write a python function to find the number of divisors of a given integer.
assert divisor(15) == 4
"""


def divisor(n):
    """
    :param n: int
    :return: int
    """
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


if __name__ == '__main__':
    print(divisor(15))
    print(divisor(10))
    print(divisor(1))
    print(divisor(2))
    print(divisor(3))
    print(divisor(4))
    print(divisor(5))
    print(divisor(6))
    print(divisor(7))
    print(divisor(8))
    print(divisor(9))
    print(divisor(10))
    print(divisor(11))
    print(divisor(12))
    print(divisor(13))
    print(divisor(14))
    print(divisor(16))
    print(divisor(17))
    print(divisor(18))
    print(divisor(19))
    print(divisor(20))
    print(divisor(21))
    print(divisor(22))
    print(divisor(23))
    print(divisor(24))
    print(divisor(25))
    print(divisor(26))
    print(divisor(27))
    print(divisor(28))
    print(divisor(29))
    print(divisor(30))
    print(divisor(31))
    print(divisor(32))
    print(divisor(33))
    print(divisor(34))
    print(divisor(35))
    print(divisor(36))
    print(divisor(37))
    print(divisor(38))
    print(divisor(39))
    print(divisor(40))
    print(divisor(41))
    print(divisor(42))
    print(divisor(43))
    print(divisor(44))
    print(divisor(45))
    print(divisor(46))
    print(divisor(47))
    print(divisor(48))
    print(divisor(49))
    print(divisor(50))
    print(divisor(51))
    print(divisor(52))
    print(divisor(53))
    print(divisor(54))
    print(divisor(55))
    print(divisor(56))
    print(divisor(57))
    print(divisor(58))
    print(divisor(59))
    print(divisor(60))
    print(divisor(61))
    print(divisor(62))
    print(divisor(63))
    print(divisor(64))
    print(divisor(65))
    print(divisor(66))
    print(divisor(67))
    print(divisor(68))
    print(divisor(69))
    print(divisor(70))
    print(divisor(71))
    print(divisor(72))
    print(divisor(73))
    print(divisor(74))