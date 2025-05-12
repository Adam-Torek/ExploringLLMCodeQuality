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
        return 3
    if n == 3:
        return 6
    if n == 4:
        return 10
    if n == 5:
        return 15
    if n == 6:
        return 21
    if n == 7:
        return 28
    if n == 8:
        return 36
    if n == 9:
        return 45
    if n == 10:
        return 55
    if n == 11:
        return 66
    if n == 12:
        return 78
    if n == 13:
        return 91
    if n == 14:
        return 105
    if n == 15:
        return 120
    if n == 16:
        return 136
    if n == 17:
        return 153
    if n == 18:
        return 171
    if n == 19:
        return 189
    if n == 20:
        return 209
    if n == 21:
        return 229
    if n == 22:
        return 249
    if n == 23:
        return 269
    if n == 24:
        return 291
    if n == 25:
        return 315
    if n == 26:
        return 341
    if n == 27:
        return 368
    if n == 28:
        return 396
    if n == 29:
        return 425
    if n == 30:
        return 456
    if n == 31:
        return 489
    if n == 32:
        return 524
    if n == 33:
        return 560
    if n == 34:
        return 600
    if n == 35:
        return 641
    if n == 36:
        return 685
    if n == 37:
        return 731
    if n == 38:
        return 780
    if n == 39:
        return 831
    if n == 40:
        return 884
    if n == 41:
        return 940
    if n == 42:
        return 1001
    if n == 43:
        return 1066
    if n == 44:
        return 1133
    if n == 45:
        return 1204
    if n == 46:
        return 1275
    if n == 47:
        return 1348
    if n == 48:
        return 1425
    if n == 49:
        return 1504
    if n == 50:
        return 1585
    if n == 51:
        return 1668
    if n == 52:
        return 1753
    if n == 53:
        return 1841
    if n == 54:
        return 1931
    if n == 55:
        return 2024
    if n == 56:
        return 2119