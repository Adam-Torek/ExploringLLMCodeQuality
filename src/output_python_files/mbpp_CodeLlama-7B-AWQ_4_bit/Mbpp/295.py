"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""


def sum_div(n):
    """
    >>> sum_div(8)
    7
    >>> sum_div(10)
    28
    >>> sum_div(12)
    28
    >>> sum_div(14)
    30
    >>> sum_div(16)
    32
    >>> sum_div(18)
    36
    >>> sum_div(20)
    42
    >>> sum_div(22)
    42
    >>> sum_div(24)
    48
    >>> sum_div(26)
    50
    >>> sum_div(28)
    56
    >>> sum_div(30)
    66
    >>> sum_div(32)
    70
    >>> sum_div(34)
    76
    >>> sum_div(36)
    82
    >>> sum_div(38)
    88
    >>> sum_div(40)
    102
    >>> sum_div(42)
    110
    >>> sum_div(44)
    118
    >>> sum_div(46)
    126
    >>> sum_div(48)
    138
    >>> sum_div(50)
    150
    >>> sum_div(52)
    162
    >>> sum_div(54)
    174
    >>> sum_div(56)
    186
    >>> sum_div(58)
    200
    >>> sum_div(60)
    222
    >>> sum_div(62)
    234
    >>> sum_div(64)
    246
    >>> sum_div(66)
    260
    >>> sum_div(68)
    274
    >>> sum_div(70)
    290
    >>> sum_div(72)
    306
    >>> sum_div(74)
    322
    >>> sum_div(76)
    338
    >>> sum_div(78)
    354
    >>> sum_div(80)
    380
    >>> sum_div(82)
    396
    >>> sum_div(84)
    412
    >>> sum_div(86)
    428
    >>> sum_div(88)
    444
    >>> sum_div(90)
    470
    >>> sum_div(92)
    486
    >>> sum_div(94)
    502
    >>> sum_div(96)
    528
    >>> sum_div(98)
    544
    >>> sum_div(100)
    570
    >>> sum_div(102)
    586
    >>> sum_div(104)
    602
    >>> sum_div(106)
    618
    >>> sum_div(108)
    634
    >>> sum_div(110)
    660
    >>> sum_div(112)
    676
    >>> sum_div(114)
    692
    >>> sum_div(116)
    708
    >>> sum_div(118)
    724
    >>> sum_div(120)
    750
    >>> sum_div(122)
    766
    >>> sum_div(124)
    7