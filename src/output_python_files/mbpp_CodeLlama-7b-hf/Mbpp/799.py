"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
assert left_rotate(16,2) == 64
"""


def left_rotate(num, d):
    """
    :param num: number to rotate
    :param d: number of bits to rotate
    :return: rotated number
    """
    mask = 0xffffffff
    return (num << d) & mask | (num >> (32 - d)) & mask


if __name__ == '__main__':
    print(left_rotate(16, 2))
    print(left_rotate(16, 3))
    print(left_rotate(16, 4))
    print(left_rotate(16, 5))
    print(left_rotate(16, 6))
    print(left_rotate(16, 7))
    print(left_rotate(16, 8))
    print(left_rotate(16, 9))
    print(left_rotate(16, 10))
    print(left_rotate(16, 11))
    print(left_rotate(16, 12))
    print(left_rotate(16, 13))
    print(left_rotate(16, 14))
    print(left_rotate(16, 15))
    print(left_rotate(16, 16))
    print(left_rotate(16, 17))
    print(left_rotate(16, 18))
    print(left_rotate(16, 19))
    print(left_rotate(16, 20))
    print(left_rotate(16, 21))
    print(left_rotate(16, 22))
    print(left_rotate(16, 23))
    print(left_rotate(16, 24))
    print(left_rotate(16, 25))
    print(left_rotate(16, 26))
    print(left_rotate(16, 27))
    print(left_rotate(16, 28))
    print(left_rotate(16, 29))
    print(left_rotate(16, 30))
    print(left_rotate(16, 31))
    print(left_rotate(16, 32))
    print(left_rotate(16, 33))
    print(left_rotate(16, 34))
    print(left_rotate(16, 35))
    print(left_rotate(16, 36))
    print(left_rotate(16, 37))
    print(left_rotate(16, 38))
    print(left_rotate(16, 39))
    print(left_rotate(16, 40))
    print(left_rotate(16, 41))
    print(left_rotate(16, 42))
    print(left_rotate(16, 43))
    print(left_rotate(16, 44))
    print(left_rotate(16, 45))
    print(left_rotate(16, 46))
    print(left_rotate(16, 47))
    print(left_rotate(16, 48))
    print(left_rotate(16, 49))
    print(left_rotate(16, 50))
    print(left_rotate(16, 51))
    print(left_rotate(16, 52))
    print(left_rotate(16, 53))
    print(left_rotate(16, 54))
    print(left_rotate(16, 55))
    print(left_rotate(16, 56))
    print(left_rotate(16, 57))
    print(left_rotate(16, 58))
    print(left_rotate(16, 59))
    print(left_rotate(16, 60))
    print(left_rotate(16