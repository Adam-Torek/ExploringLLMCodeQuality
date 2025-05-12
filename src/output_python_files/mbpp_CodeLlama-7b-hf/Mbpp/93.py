"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""


def power(a, b):
    """
    :param a: int
    :param b: int
    :return: int
    """
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a, b // 2) * power(a, b // 2)
    else:
        return a * power(a, b // 2) * power(a, b // 2)


if __name__ == '__main__':
    print(power(3, 4))
    print(power(2, 10))
    print(power(3, 3))
    print(power(2, 1))
    print(power(2, 0))
    print(power(0, 0))
    print(power(0, 1))
    print(power(0, 2))
    print(power(0, 3))
    print(power(0, 4))
    print(power(0, 5))
    print(power(0, 6))
    print(power(0, 7))
    print(power(0, 8))
    print(power(0, 9))
    print(power(0, 10))
    print(power(0, 11))
    print(power(0, 12))
    print(power(0, 13))
    print(power(0, 14))
    print(power(0, 15))
    print(power(0, 16))
    print(power(0, 17))
    print(power(0, 18))
    print(power(0, 19))
    print(power(0, 20))
    print(power(0, 21))
    print(power(0, 22))
    print(power(0, 23))
    print(power(0, 24))
    print(power(0, 25))
    print(power(0, 26))
    print(power(0, 27))
    print(power(0, 28))
    print(power(0, 29))
    print(power(0, 30))
    print(power(0, 31))
    print(power(0, 32))
    print(power(0, 33))
    print(power(0, 34))
    print(power(0, 35))
    print(power(0, 36))
    print(power(0, 37))
    print(power(0, 38))
    print(power(0, 39))
    print(power(0, 40))
    print(power(0, 41))
    print(power(0, 42))
    print(power(0, 43))
    print(power(0, 44))
    print(power(0, 45))
    print(power(0, 46))
    print(power(0, 47))
    print(power(0, 48))
    print(power(0, 49))
    print(power(0, 50))
    print(power(0, 51))
    print(power(0, 52))
    print(power(0, 53))
    print(power(0, 54))
    print(power(0, 55))
    print(power(0, 56))
    print(power(0, 57))
    print(power(0, 58))
    print(power(0, 59))
    print(power(0, 60))
    print(power(0, 61))
    print(power(0, 62))
    print(power(0, 63))
    print(power(0, 64))
    print(power(0, 65))
    print(power(0,