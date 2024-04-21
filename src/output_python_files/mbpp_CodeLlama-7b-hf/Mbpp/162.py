"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""


def sum_series(n):
    """
    >>> sum_series(6)
    12
    >>> sum_series(10)
    30
    >>> sum_series(1)
    0
    >>> sum_series(2)
    2
    >>> sum_series(3)
    3
    >>> sum_series(4)
    4
    >>> sum_series(5)
    5
    >>> sum_series(7)
    11
    >>> sum_series(8)
    16
    >>> sum_series(9)
    20
    >>> sum_series(10)
    30
    >>> sum_series(11)
    33
    >>> sum_series(12)
    36
    >>> sum_series(13)
    39
    >>> sum_series(14)
    42
    >>> sum_series(15)
    45
    >>> sum_series(16)
    48
    >>> sum_series(17)
    51
    >>> sum_series(18)
    54
    >>> sum_series(19)
    57
    >>> sum_series(20)
    60
    >>> sum_series(21)
    63
    >>> sum_series(22)
    66
    >>> sum_series(23)
    69
    >>> sum_series(24)
    72
    >>> sum_series(25)
    75
    >>> sum_series(26)
    78
    >>> sum_series(27)
    81
    >>> sum_series(28)
    84
    >>> sum_series(29)
    87
    >>> sum_series(30)
    90
    >>> sum_series(31)
    93
    >>> sum_series(32)
    96
    >>> sum_series(33)
    99
    >>> sum_series(34)
    102
    >>> sum_series(35)
    105
    >>> sum_series(36)
    108
    >>> sum_series(37)
    111
    >>> sum_series(38)
    114
    >>> sum_series(39)
    117
    >>> sum_series(40)
    120
    >>> sum_series(41)
    123
    >>> sum_series(42)
    126
    >>> sum_series(43)
    129
    >>> sum_series(44)
    132
    >>> sum_series(45)
    135
    >>> sum_series(46)
    138
    >>> sum_series(47)
    141
    >>> sum_series(48)
    144
    >>> sum_series(49)
    147
    >>> sum_series(50)
    150
    >>> sum_series(51)
    153
    >>> sum_series(52)
    156
    >>> sum_series(53)
    159
    >>> sum_series(54)
    162
    >>> sum_series(55)
    165
    >>> sum_series(56)
    168
    >>> sum_series(57)
    171
    >>> sum_series(58)
    174
    >>> sum_series(59)
    177
    >>> sum_series(60)
    180
    >>> sum_series(61)
    183
    >>> sum_series(62)
    186
    >>> sum_series(63)
    189
    >>> sum_series(64)
    192
    >>> sum_series(65)
    195