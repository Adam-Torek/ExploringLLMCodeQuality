"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""


def find_Index(n):
    """
    :param n: number of digits
    :return: index of smallest triangular number with n digits
    """
    if n == 1:
        return 1
    if n == 2:
        return 10
    if n == 3:
        return 100
    if n == 4:
        return 1000
    if n == 5:
        return 10000
    if n == 6:
        return 100000
    if n == 7:
        return 1000000
    if n == 8:
        return 10000000
    if n == 9:
        return 100000000
    if n == 10:
        return 1000000000
    if n == 11:
        return 10000000000
    if n == 12:
        return 100000000000
    if n == 13:
        return 1000000000000
    if n == 14:
        return 10000000000000
    if n == 15:
        return 100000000000000
    if n == 16:
        return 1000000000000000
    if n == 17:
        return 10000000000000000
    if n == 18:
        return 100000000000000000
    if n == 19:
        return 1000000000000000000
    if n == 20:
        return 10000000000000000000
    if n == 21:
        return 100000000000000000000
    if n == 22:
        return 1000000000000000000000
    if n == 23:
        return 10000000000000000000000
    if n == 24:
        return 100000000000000000000000
    if n == 25:
        return 1000000000000000000000000
    if n == 26:
        return 10000000000000000000000000
    if n == 27:
        return 100000000000000000000000000
    if n == 28:
        return 1000000000000000000000000000
    if n == 29:
        return 10000000000000000000000000000
    if n == 30:
        return 100000000000000000000000000000
    if n == 31:
        return 1000000000000000000000000000000
    if n == 32:
        return 100000000000000000