"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""


def square_Sum(n):
    """
    :param n: int
    :return: int
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 5
    return (n * (n + 1) * (2 * n + 1)) / 6


if __name__ == '__main__':
    print(square_Sum(2))
    print(square_Sum(3))
    print(square_Sum(4))
    print(square_Sum(5))
    print(square_Sum(6))
    print(square_Sum(7))
    print(square_Sum(8))
    print(square_Sum(9))
    print(square_Sum(10))
    print(square_Sum(11))
    print(square_Sum(12))
    print(square_Sum(13))
    print(square_Sum(14))
    print(square_Sum(15))
    print(square_Sum(16))
    print(square_Sum(17))
    print(square_Sum(18))
    print(square_Sum(19))
    print(square_Sum(20))
    print(square_Sum(21))
    print(square_Sum(22))
    print(square_Sum(23))
    print(square_Sum(24))
    print(square_Sum(25))
    print(square_Sum(26))
    print(square_Sum(27))
    print(square_Sum(28))
    print(square_Sum(29))
    print(square_Sum(30))
    print(square_Sum(31))
    print(square_Sum(32))
    print(square_Sum(33))
    print(square_Sum(34))
    print(square_Sum(35))
    print(square_Sum(36))
    print(square_Sum(37))
    print(square_Sum(38))
    print(square_Sum(39))
    print(square_Sum(40))
    print(square_Sum(41))
    print(square_Sum(42))
    print(square_Sum(43))
    print(square_Sum(44))
    print(square_Sum(45))
    print(square_Sum(46))
    print(square_Sum(47))
    print(square_Sum(48))
    print(square_Sum(49))
    print(square_Sum(50))
    print(square_Sum(51))
    print(square_Sum(52))
    print(square_Sum(53))
    print(square_Sum(54))
    print(square_Sum(55))
    print(square_Sum(56))
    print(square_Sum(57))
    print(square_Sum(58))
    print(square_Sum(59))
    print(square_Sum(60))
    print(square_Sum(61))
    print(square_Sum(62))
    print(square_Sum(63))
    print(square_Sum(64))
    print(square_Sum(65))
    print(square_Sum(66))
    print(square_Sum(67))
    print(square_Sum(68))
    print(square_Sum(69))
    print(square_Sum(70))
    print(square_Sum(71))
    print(square_Sum(72))
    print(square_Sum(73))
    print(square_Sum(74))
    print(square_Sum(75))
    print(square_Sum(76))
    print(square_Sum(77))
    print(square_Sum(78))