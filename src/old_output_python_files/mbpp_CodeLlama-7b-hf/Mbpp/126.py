"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""


def sum(a, b):
    """
    :param a: int
    :param b: int
    :return: int
    """
    if a < b:
        a, b = b, a
    result = 0
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            result += i
    return result


if __name__ == '__main__':
    print(sum(10, 15))
    print(sum(10, 10))
    print(sum(10, 11))
    print(sum(10, 12))
    print(sum(10, 13))
    print(sum(10, 14))
    print(sum(10, 15))
    print(sum(10, 16))
    print(sum(10, 17))
    print(sum(10, 18))
    print(sum(10, 19))
    print(sum(10, 20))
    print(sum(10, 21))
    print(sum(10, 22))
    print(sum(10, 23))
    print(sum(10, 24))
    print(sum(10, 25))
    print(sum(10, 26))
    print(sum(10, 27))
    print(sum(10, 28))
    print(sum(10, 29))
    print(sum(10, 30))
    print(sum(10, 31))
    print(sum(10, 32))
    print(sum(10, 33))
    print(sum(10, 34))
    print(sum(10, 35))
    print(sum(10, 36))
    print(sum(10, 37))
    print(sum(10, 38))
    print(sum(10, 39))
    print(sum(10, 40))
    print(sum(10, 41))
    print(sum(10, 42))
    print(sum(10, 43))
    print(sum(10, 44))
    print(sum(10, 45))
    print(sum(10, 46))
    print(sum(10, 47))
    print(sum(10, 48))
    print(sum(10, 49))
    print(sum(10, 50))
    print(sum(10, 51))
    print(sum(10, 52))
    print(sum(10, 53))
    print(sum(10, 54))
    print(sum(10, 55))
    print(sum(10, 56))
    print(sum(10, 57))
    print(sum(10, 58))
    print(sum(10, 59))
    print(sum(10, 60))
    print(sum(10, 61))
    print(sum(10, 62))
    print(sum(10, 63))
    print(sum(10, 64))
    print(sum(10, 65))
    print(sum(10, 66))
    print(sum(10, 67))
    print(sum(10, 68))
    print(sum(10, 69))
    print(sum(10, 70))
    print(sum(10, 71))
    print(sum(10, 72))
    print(sum(10, 73))
    print(sum(10, 74))
    print(sum(10, 75))
    print(sum(