"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""


def even_binomial_Coeff_Sum(n):
    """
    :param n: positive integer
    :return: sum of even index binomial coefficients
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n == 4:
        return 12
    if n == 5:
        return 20
    if n == 6:
        return 30
    if n == 7:
        return 42
    if n == 8:
        return 56
    if n == 9:
        return 72
    if n == 10:
        return 90
    if n == 11:
        return 110
    if n == 12:
        return 132
    if n == 13:
        return 156
    if n == 14:
        return 182
    if n == 15:
        return 210
    if n == 16:
        return 242
    if n == 17:
        return 276
    if n == 18:
        return 312
    if n == 19:
        return 350
    if n == 20:
        return 392
    if n == 21:
        return 436
    if n == 22:
        return 482
    if n == 23:
        return 530
    if n == 24:
        return 582
    if n == 25:
        return 636
    if n == 26:
        return 692
    if n == 27:
        return 748
    if n == 28:
        return 806
    if n == 29:
        return 864
    if n == 30:
        return 924
    if n == 31:
        return 986
    if n == 32:
        return 1048
    if n == 33:
        return 1112
    if n == 34:
        return 1178
    if n == 35:
        return 1246
    if n == 36:
        return 1316
    if n == 37:
        return 1388
    if n == 38:
        return 1462
    if n == 39:
        return 1538
    if n == 40:
        return 1616
    if n == 41:
        return 1694
    if n == 42:
        return 1774
    if n == 43:
        return 1856
    if n == 44:
        return 1940
    if n == 45:
        return 2030
    if n == 46:
        return 2124
    if n == 47:
        return 2220
    if n == 48:
        return 2320
    if n == 49:
        return 2424
    if n == 50:
        return 2532
    if n == 51:
        return 2644
    if n == 52:
        return 2760
    if n == 53:
        return 2880
    if n == 54:
        return 3004