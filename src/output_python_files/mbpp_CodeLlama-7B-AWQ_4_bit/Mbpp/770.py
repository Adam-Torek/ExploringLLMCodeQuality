"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""


def odd_num_sum(n):
    """
    >>> odd_num_sum(2)
    82
    >>> odd_num_sum(3)
    265
    >>> odd_num_sum(4)
    510
    >>> odd_num_sum(5)
    857
    >>> odd_num_sum(6)
    1212
    >>> odd_num_sum(7)
    1665
    >>> odd_num_sum(8)
    2120
    >>> odd_num_sum(9)
    2677
    >>> odd_num_sum(10)
    3232
    >>> odd_num_sum(11)
    3795
    >>> odd_num_sum(12)
    4358
    >>> odd_num_sum(13)
    4921
    >>> odd_num_sum(14)
    5584
    >>> odd_num_sum(15)
    6247
    >>> odd_num_sum(16)
    6910
    >>> odd_num_sum(17)
    7573
    >>> odd_num_sum(18)
    8236
    >>> odd_num_sum(19)
    8900
    >>> odd_num_sum(20)
    9573
    >>> odd_num_sum(21)
    10246
    >>> odd_num_sum(22)
    10920
    >>> odd_num_sum(23)
    11603
    >>> odd_num_sum(24)
    12286
    >>> odd_num_sum(25)
    13060
    >>> odd_num_sum(26)
    13843
    >>> odd_num_sum(27)
    14626
    >>> odd_num_sum(28)
    15410
    >>> odd_num_sum(29)
    16203
    >>> odd_num_sum(30)
    17000
    >>> odd_num_sum(31)
    17800
    >>> odd_num_sum(32)
    18600
    >>> odd_num_sum(33)
    19400
    >>> odd_num_sum(34)
    20200
    >>> odd_num_sum(35)
    21000
    >>> odd_num_sum(36)
    21800
    >>> odd_num_sum(37)
    22600
    >>> odd_num_sum(38)
    23400
    >>> odd_num_sum(39)
    24200
    >>> odd_num_sum(40)
    25000
    >>> odd_num_sum(41)
    25800
    >>> odd_num_sum(42)
    26600
    >>> odd_num_sum(43)
    27400
    >>> odd_num_sum(44)
    28200
    >>> odd_num_sum(45)
    29000
    >>> odd_num_sum(46)
    29800
    >>> odd_num_sum(47)
    30600
    >>> odd_num_sum(48)
    31400
    >>> odd_num_sum(49)
    32200
    >>> odd_num_sum(50)
    33000
    >>> odd_num_sum(51)
    33800
    >>> odd_num_sum(52)