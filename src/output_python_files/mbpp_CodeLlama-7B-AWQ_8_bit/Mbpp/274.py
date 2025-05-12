"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""


def even_binomial_Coeff_Sum(n):
    """
    :param n: positive integer
    :return: sum of even index binomial coefficients
    """
    return sum(binomial_coefficient(n, i) for i in range(n + 1) if i % 2 == 0)


def binomial_coefficient(n, k):
    """
    :param n: positive integer
    :param k: positive integer
    :return: binomial coefficient
    """
    return factorial(n) / (factorial(k) * factorial(n - k))


def factorial(n):
    """
    :param n: positive integer
    :return: factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    print(even_binomial_Coeff_Sum(4))
    print(binomial_coefficient(4, 2))
    print(factorial(4))
    print(factorial(0))
    print(factorial(1))
    print(factorial(2))
    print(factorial(3))
    print(factorial(4))
    print(factorial(5))
    print(factorial(6))
    print(factorial(7))
    print(factorial(8))
    print(factorial(9))
    print(factorial(10))
    print(factorial(11))
    print(factorial(12))
    print(factorial(13))
    print(factorial(14))
    print(factorial(15))
    print(factorial(16))
    print(factorial(17))
    print(factorial(18))
    print(factorial(19))
    print(factorial(20))
    print(factorial(21))
    print(factorial(22))
    print(factorial(23))
    print(factorial(24))
    print(factorial(25))
    print(factorial(26))
    print(factorial(27))
    print(factorial(28))
    print(factorial(29))
    print(factorial(30))
    print(factorial(31))
    print(factorial(32))
    print(factorial(33))
    print(factorial(34))
    print(factorial(35))
    print(factorial(36))
    print(factorial(37))
    print(factorial(38))
    print(factorial(39))
    print(factorial(40))
    print(factorial(41))
    print(factorial(42))
    print(factorial(43))
    print(factorial(44))
    print(factorial(45))
    print(factorial(46))
    print(factorial(47))
    print(factorial(48))
    print(factorial(49))
    print(factorial(50))
    print(factorial(51))
    print(factorial(52))
    print(factorial(53))
    print(factorial(54))
    print(factorial(55))
    print(factorial(56))
    print(factorial(57))
    print(factorial(58))
    print(factorial(59))
    print(factorial(60))
    print(factorial(61))
    print(factorial(62))
    print(factorial(63))
    print(factorial(64))
    print(factorial(65))
    print(factorial(66))
    print(factorial(67))
    print(factorial(68))
    print(factorial(69))
    print(factorial(70))
    print(factorial(71))
    print(factorial(7