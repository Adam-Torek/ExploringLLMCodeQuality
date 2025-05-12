"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""


def sumofFactors(n):
    """
    :param n: int
    :return: int
    """
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
    return sum


if __name__ == '__main__':
    print(sumofFactors(18))
    print(sumofFactors(10))
    print(sumofFactors(12))
    print(sumofFactors(14))
    print(sumofFactors(16))
    print(sumofFactors(18))
    print(sumofFactors(20))
    print(sumofFactors(22))
    print(sumofFactors(24))
    print(sumofFactors(26))
    print(sumofFactors(28))
    print(sumofFactors(30))
    print(sumofFactors(32))
    print(sumofFactors(34))
    print(sumofFactors(36))
    print(sumofFactors(38))
    print(sumofFactors(40))
    print(sumofFactors(42))
    print(sumofFactors(44))
    print(sumofFactors(46))
    print(sumofFactors(48))
    print(sumofFactors(50))
    print(sumofFactors(52))
    print(sumofFactors(54))
    print(sumofFactors(56))
    print(sumofFactors(58))
    print(sumofFactors(60))
    print(sumofFactors(62))
    print(sumofFactors(64))
    print(sumofFactors(66))
    print(sumofFactors(68))
    print(sumofFactors(70))
    print(sumofFactors(72))
    print(sumofFactors(74))
    print(sumofFactors(76))
    print(sumofFactors(78))
    print(sumofFactors(80))
    print(sumofFactors(82))
    print(sumofFactors(84))
    print(sumofFactors(86))
    print(sumofFactors(88))
    print(sumofFactors(90))
    print(sumofFactors(92))
    print(sumofFactors(94))
    print(sumofFactors(96))
    print(sumofFactors(98))
    print(sumofFactors(100))
    print(sumofFactors(102))
    print(sumofFactors(104))
    print(sumofFactors(106))
    print(sumofFactors(108))
    print(sumofFactors(110))
    print(sumofFactors(112))
    print(sumofFactors(114))
    print(sumofFactors(116))
    print(sumofFactors(118))
    print(sumofFactors(120))
    print(sumofFactors(122))
    print(sumofFactors(124))
    print(sumofFactors(126))
    print(sumofFactors(128))
    print(sumofFactors(130))
    print(sumofFactors(132))
    print(sumofFactors(134))
    print(sumofFactors(136))
    print(sumofFactors(138))
    print(sumofFactors(140))
    print(sumofFactors(142))
    print(sumofFactors(144))
    print(sumofFactors(146))
    print(sumofFactors(148))
    print(sumofFactors(150))
    print(sumofFact