"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""


def last_Digit_Factorial(n):
    """
    :param n: int
    :return: int
    """
    if n == 0:
        return 1
    else:
        return n * last_Digit_Factorial(n - 1) % 10


if __name__ == '__main__':
    print(last_Digit_Factorial(4))
    print(last_Digit_Factorial(5))
    print(last_Digit_Factorial(6))
    print(last_Digit_Factorial(7))
    print(last_Digit_Factorial(8))
    print(last_Digit_Factorial(9))
    print(last_Digit_Factorial(10))
    print(last_Digit_Factorial(11))
    print(last_Digit_Factorial(12))
    print(last_Digit_Factorial(13))
    print(last_Digit_Factorial(14))
    print(last_Digit_Factorial(15))
    print(last_Digit_Factorial(16))
    print(last_Digit_Factorial(17))
    print(last_Digit_Factorial(18))
    print(last_Digit_Factorial(19))
    print(last_Digit_Factorial(20))
    print(last_Digit_Factorial(21))
    print(last_Digit_Factorial(22))
    print(last_Digit_Factorial(23))
    print(last_Digit_Factorial(24))
    print(last_Digit_Factorial(25))
    print(last_Digit_Factorial(26))
    print(last_Digit_Factorial(27))
    print(last_Digit_Factorial(28))
    print(last_Digit_Factorial(29))
    print(last_Digit_Factorial(30))
    print(last_Digit_Factorial(31))
    print(last_Digit_Factorial(32))
    print(last_Digit_Factorial(33))
    print(last_Digit_Factorial(34))
    print(last_Digit_Factorial(35))
    print(last_Digit_Factorial(36))
    print(last_Digit_Factorial(37))
    print(last_Digit_Factorial(38))
    print(last_Digit_Factorial(39))
    print(last_Digit_Factorial(40))
    print(last_Digit_Factorial(41))
    print(last_Digit_Factorial(42))
    print(last_Digit_Factorial(43))
    print(last_Digit_Factorial(44))
    print(last_Digit_Factorial(45))
    print(last_Digit_Factorial(46))
    print(last_Digit_Factorial(47))
    print(last_Digit_Factorial(48))
    print(last_Digit_Factorial(49))
    print(last_Digit_Factorial(50))
    print(last_Digit_Factorial(51))
    print(last_Digit_Factorial(52))
    print(last_Digit_Factorial(53))
    print(last_Digit_Factorial(54))
    print(last_Digit_Factorial(55))
    print(last_Digit_Factorial(56))
    print(last_Digit_Factorial(57))
    print(last_Digit_Factorial(58))
    print(last_Digit_Factorial(59))
    print(last_Digit