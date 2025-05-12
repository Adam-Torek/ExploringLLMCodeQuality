"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""


def differ_At_One_Bit_Pos(a, b):
    """
    :param a: int
    :param b: int
    :return: bool
    """
    return bin(a ^ b).count('1') == 1


if __name__ == '__main__':
    print(differ_At_One_Bit_Pos(13, 9))
    print(differ_At_One_Bit_Pos(13, 13))
    print(differ_At_One_Bit_Pos(13, 14))
    print(differ_At_One_Bit_Pos(13, 15))
    print(differ_At_One_Bit_Pos(13, 16))
    print(differ_At_One_Bit_Pos(13, 17))
    print(differ_At_One_Bit_Pos(13, 18))
    print(differ_At_One_Bit_Pos(13, 19))
    print(differ_At_One_Bit_Pos(13, 20))
    print(differ_At_One_Bit_Pos(13, 21))
    print(differ_At_One_Bit_Pos(13, 22))
    print(differ_At_One_Bit_Pos(13, 23))
    print(differ_At_One_Bit_Pos(13, 24))
    print(differ_At_One_Bit_Pos(13, 25))
    print(differ_At_One_Bit_Pos(13, 26))
    print(differ_At_One_Bit_Pos(13, 27))
    print(differ_At_One_Bit_Pos(13, 28))
    print(differ_At_One_Bit_Pos(13, 29))
    print(differ_At_One_Bit_Pos(13, 30))
    print(differ_At_One_Bit_Pos(13, 31))
    print(differ_At_One_Bit_Pos(13, 32))
    print(differ_At_One_Bit_Pos(13, 33))
    print(differ_At_One_Bit_Pos(13, 34))
    print(differ_At_One_Bit_Pos(13, 35))
    print(differ_At_One_Bit_Pos(13, 36))
    print(differ_At_One_Bit_Pos(13, 37))
    print(differ_At_One_Bit_Pos(13, 38))
    print(differ_At_One_Bit_Pos(13, 39))
    print(differ_At_One_Bit_Pos(13, 40))
    print(differ_At_One_Bit_Pos(13, 41))
    print(differ_At_One_Bit_Pos(13, 42))
    print(differ_At_One_Bit_Pos(13, 43))
    print(differ_At_One_Bit_Pos(13, 44))
    print(differ_At_One_Bit_Pos(13, 45))
    print(differ_At_One_Bit_Pos(13, 46))
    print(differ_At_One_Bit_Pos(13, 47))
    print(differ_At_One_Bit_Pos(13, 48))
    print(differ_At_One_Bit_Pos(13, 49))
    print(differ_At_One_Bit_Pos(13, 50))
    print(differ_At_One_Bit_Pos(13, 51))
    print(differ_At_One_Bit_Pos(13, 52))
    print(differ