"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""

import math


def count_binary_seq(n):
    """
    :param n: int
    :return: float
    """
    if n == 1:
        return 2.0
    else:
        return 2.0 * count_binary_seq(n - 1) + 2.0 * count_binary_seq(n - 2)


if __name__ == '__main__':
    print(count_binary_seq(1))
    print(count_binary_seq(2))
    print(count_binary_seq(3))
    print(count_binary_seq(4))
    print(count_binary_seq(5))
    print(count_binary_seq(6))
    print(count_binary_seq(7))
    print(count_binary_seq(8))
    print(count_binary_seq(9))
    print(count_binary_seq(10))
    print(count_binary_seq(11))
    print(count_binary_seq(12))
    print(count_binary_seq(13))
    print(count_binary_seq(14))
    print(count_binary_seq(15))
    print(count_binary_seq(16))
    print(count_binary_seq(17))
    print(count_binary_seq(18))
    print(count_binary_seq(19))
    print(count_binary_seq(20))
    print(count_binary_seq(21))
    print(count_binary_seq(22))
    print(count_binary_seq(23))
    print(count_binary_seq(24))
    print(count_binary_seq(25))
    print(count_binary_seq(26))
    print(count_binary_seq(27))
    print(count_binary_seq(28))
    print(count_binary_seq(29))
    print(count_binary_seq(30))
    print(count_binary_seq(31))
    print(count_binary_seq(32))
    print(count_binary_seq(33))
    print(count_binary_seq(34))
    print(count_binary_seq(35))
    print(count_binary_seq(36))
    print(count_binary_seq(37))
    print(count_binary_seq(38))
    print(count_binary_seq(39))
    print(count_binary_seq(40))
    print(count_binary_seq(41))
    print(count_binary_seq(42))
    print(count_binary_seq(43))
    print(count_binary_seq(44))
    print(count_binary_seq(45))
    print(count_binary_seq(46))
    print(count_binary_seq(47))
    print(count_binary_seq(48))
    print(count_binary_seq(49))
    print(count_binary_seq(50))
    print(count_binary_seq(51))
    print(count_binary_seq(52))
    print(count_binary_seq(53))
    print(count_binary_seq(54))
    print(count_binary_seq(55))
    print(count_binary_seq(56))
    print(count_binary_seq(57))
    print(count_binary_seq(58))
    print(count_binary_seq(59))
    print(count_binary_seq(60))
    print(count_binary_seq(61))
    print(count_binary_seq(62))
    print(count_binary_seq(63))
    print(count_binary_seq(64))
    print(count_binary_seq(65))
    print(count_binary_seq(66))
    print(