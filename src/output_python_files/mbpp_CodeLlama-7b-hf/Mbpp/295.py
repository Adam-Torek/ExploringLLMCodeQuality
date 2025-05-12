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
    30
    >>> sum_div(14)
    36
    >>> sum_div(16)
    48
    >>> sum_div(18)
    54
    >>> sum_div(20)
    70
    >>> sum_div(22)
    76
    >>> sum_div(24)
    84
    >>> sum_div(26)
    90
    >>> sum_div(28)
    96
    >>> sum_div(30)
    110
    >>> sum_div(32)
    120
    >>> sum_div(34)
    126
    >>> sum_div(36)
    132
    >>> sum_div(38)
    138
    >>> sum_div(40)
    150
    >>> sum_div(42)
    156
    >>> sum_div(44)
    162
    >>> sum_div(46)
    168
    >>> sum_div(48)
    176
    >>> sum_div(50)
    190
    >>> sum_div(52)
    196
    >>> sum_div(54)
    202
    >>> sum_div(56)
    208
    >>> sum_div(58)
    214
    >>> sum_div(60)
    230
    >>> sum_div(62)
    236
    >>> sum_div(64)
    242
    >>> sum_div(66)
    248
    >>> sum_div(68)
    254
    >>> sum_div(70)
    270
    >>> sum_div(72)
    276
    >>> sum_div(74)
    282
    >>> sum_div(76)
    288
    >>> sum_div(78)
    294
    >>> sum_div(80)
    310
    >>> sum_div(82)
    316
    >>> sum_div(84)
    322
    >>> sum_div(86)
    328
    >>> sum_div(88)
    334
    >>> sum_div(90)
    350
    >>> sum_div(92)
    356
    >>> sum_div(94)
    362
    >>> sum_div(96)
    368
    >>> sum_div(98)
    374
    >>> sum_div(100)
    390
    >>> sum_div(102)
    396
    >>> sum_div(104)
    402
    >>> sum_div(106)
    408
    >>> sum_div(108)
    414
    >>> sum_div(110)
    430
    >>> sum_div(112)
    436
    >>> sum_div(114)
    442
    >>> sum_div(116)
    448
    >>> sum_div(118)
    454
    >>> sum_div(120)
    470
    >>> sum_div(122)
    476
    >>> sum_div(12