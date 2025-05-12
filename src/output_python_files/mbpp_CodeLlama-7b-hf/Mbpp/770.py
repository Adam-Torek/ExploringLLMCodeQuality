"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""


def odd_num_sum(n):
    """
    :param n: int
    :return: int
    """
    if n < 1:
        return 0
    else:
        return sum(i ** 4 for i in range(1, n + 1, 2))


if __name__ == '__main__':
    print(odd_num_sum(2))
    print(odd_num_sum(3))
    print(odd_num_sum(4))
    print(odd_num_sum(5))
    print(odd_num_sum(6))
    print(odd_num_sum(7))
    print(odd_num_sum(8))
    print(odd_num_sum(9))
    print(odd_num_sum(10))
    print(odd_num_sum(11))
    print(odd_num_sum(12))
    print(odd_num_sum(13))
    print(odd_num_sum(14))
    print(odd_num_sum(15))
    print(odd_num_sum(16))
    print(odd_num_sum(17))
    print(odd_num_sum(18))
    print(odd_num_sum(19))
    print(odd_num_sum(20))
    print(odd_num_sum(21))
    print(odd_num_sum(22))
    print(odd_num_sum(23))
    print(odd_num_sum(24))
    print(odd_num_sum(25))
    print(odd_num_sum(26))
    print(odd_num_sum(27))
    print(odd_num_sum(28))
    print(odd_num_sum(29))
    print(odd_num_sum(30))
    print(odd_num_sum(31))
    print(odd_num_sum(32))
    print(odd_num_sum(33))
    print(odd_num_sum(34))
    print(odd_num_sum(35))
    print(odd_num_sum(36))
    print(odd_num_sum(37))
    print(odd_num_sum(38))
    print(odd_num_sum(39))
    print(odd_num_sum(40))
    print(odd_num_sum(41))
    print(odd_num_sum(42))
    print(odd_num_sum(43))
    print(odd_num_sum(44))
    print(odd_num_sum(45))
    print(odd_num_sum(46))
    print(odd_num_sum(47))
    print(odd_num_sum(48))
    print(odd_num_sum(49))
    print(odd_num_sum(50))
    print(odd_num_sum(51))
    print(odd_num_sum(52))
    print(odd_num_sum(53))
    print(odd_num_sum(54))
    print(odd_num_sum(55))
    print(odd_num_sum(56))
    print(odd_num_sum(57))
    print(odd_num_sum(58))
    print(odd_num_sum(59))
    print(odd_num_sum(60))
    print(odd_num_sum(61))
    print(odd_num_sum(62))
    print(odd_num_sum(63))
    print(odd_num_sum(64))
    print(odd_num_sum(65))
    print(odd_num_sum(66))
    print(odd_num_sum(67))
    print(odd_num_sum(