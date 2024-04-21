"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""


def odd_Equivalent(binary_string, rotations):
    """
    :param binary_string: string
    :param rotations: int
    :return: int
    """
    binary_string = binary_string[::-1]
    for _ in range(rotations):
        binary_string = binary_string[1:] + binary_string[0]
    return binary_string.count("1")


if __name__ == '__main__':
    print(odd_Equivalent("011001", 6))
    print(odd_Equivalent("1011101", 2))
    print(odd_Equivalent("1011101", 3))
    print(odd_Equivalent("1011101", 4))
    print(odd_Equivalent("1011101", 5))
    print(odd_Equivalent("1011101", 6))
    print(odd_Equivalent("1011101", 7))
    print(odd_Equivalent("1011101", 8))
    print(odd_Equivalent("1011101", 9))
    print(odd_Equivalent("1011101", 10))
    print(odd_Equivalent("1011101", 11))
    print(odd_Equivalent("1011101", 12))
    print(odd_Equivalent("1011101", 13))
    print(odd_Equivalent("1011101", 14))
    print(odd_Equivalent("1011101", 15))
    print(odd_Equivalent("1011101", 16))
    print(odd_Equivalent("1011101", 17))
    print(odd_Equivalent("1011101", 18))
    print(odd_Equivalent("1011101", 19))
    print(odd_Equivalent("1011101", 20))
    print(odd_Equivalent("1011101", 21))
    print(odd_Equivalent("1011101", 22))
    print(odd_Equivalent("1011101", 23))
    print(odd_Equivalent("1011101", 24))
    print(odd_Equivalent("1011101", 25))
    print(odd_Equivalent("1011101", 26))
    print(odd_Equivalent("1011101", 27))
    print(odd_Equivalent("1011101", 28))
    print(odd_Equivalent("1011101", 29))
    print(odd_Equivalent("1011101", 30))
    print(odd_Equivalent("1011101", 31))
    print(odd_Equivalent("1011101", 32))
    print(odd_Equivalent("1011101", 33))
    print(odd_Equivalent("1011101", 34))
    print(odd_Equivalent("1011101", 35))
    print(odd_Equivalent("1011101", 36))
    print(odd_Equivalent("1011101", 37))
    print(odd_Equivalent("1011101", 38))
    print(odd_Equivalent("1011101", 39))
    print(odd_Equivalent("1011101", 40))
    print(odd_Equivalent("1011101", 41))
    print(odd_Equivalent("1