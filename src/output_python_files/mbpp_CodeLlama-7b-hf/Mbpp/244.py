"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""


def next_Perfect_Square(n):
    """
    :param n: int
    :return: int
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return 1
    if n == 1:
        return 4
    if n == 2:
        return 9
    if n == 3:
        return 16
    if n == 4:
        return 25
    if n == 5:
        return 36
    if n == 6:
        return 49
    if n == 7:
        return 64
    if n == 8:
        return 81
    if n == 9:
        return 100
    if n == 10:
        return 121
    if n == 11:
        return 144
    if n == 12:
        return 169
    if n == 13:
        return 196
    if n == 14:
        return 225
    if n == 15:
        return 256
    if n == 16:
        return 289
    if n == 17:
        return 324
    if n == 18:
        return 361
    if n == 19:
        return 400
    if n == 20:
        return 441
    if n == 21:
        return 484
    if n == 22:
        return 529
    if n == 23:
        return 576
    if n == 24:
        return 625
    if n == 25:
        return 676
    if n == 26:
        return 729
    if n == 27:
        return 784
    if n == 28:
        return 841
    if n == 29:
        return 900
    if n == 30:
        return 961
    if n == 31:
        return 1024
    if n == 32:
        return 1089
    if n == 33:
        return 1156
    if n == 34:
        return 1225
    if n == 35:
        return 1296
    if n == 36:
        return 1369
    if n == 37:
        return 1444
    if n == 38:
        return 1521
    if n == 39:
        return 1600
    if n == 40:
        return 1681
    if n == 41:
        return 1764
    if n == 42:
        return 1849
    if n == 43:
        return 1936
    if n == 44:
        return 2025
    if n == 45:
        return 2116
    if n == 46:
        return 2209
    if n == 47:
        return 2304
    if n == 48:
        return 2401
    if n == 49:
        return 2500
    if n == 50:
        return 2601
    if n == 51:
        return 2704
    if n == 52:
        return 2809
    if n == 53:
        return 2916
    if n == 54:
        return 3025
    if n == 55:
        return 3136
    if n == 56:
        return 3249
    if n == 57:
        return 33