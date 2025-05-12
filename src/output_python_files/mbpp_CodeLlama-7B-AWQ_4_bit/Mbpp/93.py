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
    print(power(3, 1))
    print(power(3, 2))
    print(power(3, 3))
    print(power(3, 4))
    print(power(3, 5))
    print(power(3, 6))
    print(power(3, 7))
    print(power(3, 8))
    print(power(3, 9))
    print(power(3, 10))
    print(power(3, 11))
    print(power(3, 12))
    print(power(3, 13))
    print(power(3, 14))
    print(power(3, 15))
    print(power(3, 16))
    print(power(3, 17))
    print(power(3, 18))
    print(power(3, 19))
    print(power(3, 20))
    print(power(3, 21))
    print(power(3, 22))
    print(power(3, 23))
    print(power(3, 24))
    print(power(3, 25))
    print(power(3, 26))
    print(power(3, 27))
    print(power(3, 28))
    print(power(3, 29))
    print(power(3, 30))
    print(power(3, 31))
    print(power(3, 32))
    print(power(3, 33))
    print(power(3, 34))
    print(power(3, 35))
    print(power(3, 36))
    print(power(3, 37))
    print(power(3, 38))
    print(power(3, 39))
    print(power(3, 40))
    print(power(3, 41))
    print(power(3, 42))
    print(power(3, 43))
    print(power(3, 44))
    print(power(3, 45))
    print(power(3, 46))
    print(power(3, 47))
    print(power(3, 48))
    print(power(3, 49))
    print(power(3, 50))
    print(power(3, 51))
    print(power(3, 52))
    print(power(3, 53))
    print(power(3, 54))
    print(power(3, 55))
    print(power(3, 56))
    print(power(3, 57))
    print(power(3, 58))
    print(power(3, 59))
    print(power(3, 60))
    print(power(3, 61))
    print(power(3, 62))
    print(power(3, 63))
    print(power(3, 64))
    print(power(3, 65))
    print(power(3, 66))
    print(power(3,