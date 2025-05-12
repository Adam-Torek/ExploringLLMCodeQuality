"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""


def even_binomial_Coeff_Sum(n):
    """
    >>> even_binomial_Coeff_Sum(4)
    8
    >>> even_binomial_Coeff_Sum(5)
    18
    >>> even_binomial_Coeff_Sum(6)
    32
    >>> even_binomial_Coeff_Sum(7)
    56
    >>> even_binomial_Coeff_Sum(8)
    88
    >>> even_binomial_Coeff_Sum(9)
    124
    >>> even_binomial_Coeff_Sum(10)
    176
    >>> even_binomial_Coeff_Sum(11)
    240
    >>> even_binomial_Coeff_Sum(12)
    328
    >>> even_binomial_Coeff_Sum(13)
    420
    >>> even_binomial_Coeff_Sum(14)
    528
    >>> even_binomial_Coeff_Sum(15)
    648
    >>> even_binomial_Coeff_Sum(16)
    800
    >>> even_binomial_Coeff_Sum(17)
    968
    >>> even_binomial_Coeff_Sum(18)
    1160
    >>> even_binomial_Coeff_Sum(19)
    1388
    >>> even_binomial_Coeff_Sum(20)
    1640
    >>> even_binomial_Coeff_Sum(21)
    1928
    >>> even_binomial_Coeff_Sum(22)
    2280
    >>> even_binomial_Coeff_Sum(23)
    2608
    >>> even_binomial_Coeff_Sum(24)
    2960
    >>> even_binomial_Coeff_Sum(25)
    3368
    >>> even_binomial_Coeff_Sum(26)
    3816
    >>> even_binomial_Coeff_Sum(27)
    4368
    >>> even_binomial_Coeff_Sum(28)
    4960
    >>> even_binomial_Coeff_Sum(29)
    5648
    >>> even_binomial_Coeff_Sum(30)
    6400
    >>> even_binomial_Coeff_Sum(31)
    7232
    >>> even_binomial_Coeff_Sum(32)
    8128
    >>> even_binomial_Coeff_Sum(33)
    9160
    >>> even_binomial_Coeff_Sum(34)
    10288
    >>> even_binomial_Coeff_Sum(35)
    11480
    >>> even_binomial_Coeff_Sum(36)
    12832
    >>> even_binomial_Coeff_Sum(37)
    14288
    >>> even_binomial_Coeff_Sum(38)
    15880
    >>> even_binomial_Coeff_Sum(39)
    17648
    >>> even_binomial_Coeff_Sum(40)
    19560
    >>> even_binomial_Coeff_Sum(41)
    21632
    >>> even_binomial_Coeff_Sum(42)
    23888
    >>> even_binomial_Coeff_Sum(43)
    26384
    >>> even_binomial_Coeff_Sum(44)
    28980
    >>> even_binomial_Coeff_Sum(45)
    32032
    >>> even_bin