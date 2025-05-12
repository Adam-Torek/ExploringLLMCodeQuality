"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""


def odd_num_sum(n):
    """
    >>> odd_num_sum(2)
    82
    >>> odd_num_sum(3)
    210
    >>> odd_num_sum(4)
    420
    >>> odd_num_sum(5)
    880
    >>> odd_num_sum(6)
    1500
    >>> odd_num_sum(7)
    2420
    >>> odd_num_sum(8)
    3900
    >>> odd_num_sum(9)
    6020
    >>> odd_num_sum(10)
    9260
    >>> odd_num_sum(11)
    13280
    >>> odd_num_sum(12)
    18400
    >>> odd_num_sum(13)
    25040
    >>> odd_num_sum(14)
    33280
    >>> odd_num_sum(15)
    43680
    >>> odd_num_sum(16)
    55360
    >>> odd_num_sum(17)
    68520
    >>> odd_num_sum(18)
    83160
    >>> odd_num_sum(19)
    100000
    >>> odd_num_sum(20)
    121600
    >>> odd_num_sum(21)
    145600
    >>> odd_num_sum(22)
    171600
    >>> odd_num_sum(23)
    199200
    >>> odd_num_sum(24)
    230400
    >>> odd_num_sum(25)
    262400
    >>> odd_num_sum(26)
    296400
    >>> odd_num_sum(27)
    332400
    >>> odd_num_sum(28)
    370400
    >>> odd_num_sum(29)
    410400
    >>> odd_num_sum(30)
    452400
    >>> odd_num_sum(31)
    500400
    >>> odd_num_sum(32)
    550400
    >>> odd_num_sum(33)
    604400
    >>> odd_num_sum(34)
    660400
    >>> odd_num_sum(35)
    720400
    >>> odd_num_sum(36)
    784400
    >>> odd_num_sum(37)
    852400
    >>> odd_num_sum(38)
    924400
    >>> odd_num_sum(39)
    998400
    >>> odd_num_sum(40)
    1076400
    >>> odd_num_sum(41)
    1156400
    >>> odd_num_sum(42)
    1240400
    >>> odd_num_sum(43)
    1330400
    >>> odd_num_sum(44)
    1430400
    >>> odd_num_sum(45)
    1536400
    >>> odd_num_sum(46)
    1644400
    >>> odd_num_sum(47)
    1756400
    >>> odd_num_sum(48)
    1872400
    >>> odd_num_sum(49)
    2000400
    >>> odd_num_sum(50)
    2132400
    >>> odd_num_sum(51)
    22704