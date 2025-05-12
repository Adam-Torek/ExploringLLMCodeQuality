"""
Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
assert even_Power_Sum(2) == 1056
"""


def even_Power_Sum(n):
    """
    >>> even_Power_Sum(2)
    1056
    >>> even_Power_Sum(3)
    3025
    >>> even_Power_Sum(4)
    6046
    >>> even_Power_Sum(5)
    10055
    >>> even_Power_Sum(6)
    16066
    >>> even_Power_Sum(7)
    26077
    >>> even_Power_Sum(8)
    40088
    >>> even_Power_Sum(9)
    60100
    >>> even_Power_Sum(10)
    80112
    >>> even_Power_Sum(11)
    100124
    >>> even_Power_Sum(12)
    120136
    >>> even_Power_Sum(13)
    140148
    >>> even_Power_Sum(14)
    160160
    >>> even_Power_Sum(15)
    180172
    >>> even_Power_Sum(16)
    200184
    >>> even_Power_Sum(17)
    220196
    >>> even_Power_Sum(18)
    240208
    >>> even_Power_Sum(19)
    260220
    >>> even_Power_Sum(20)
    280232
    >>> even_Power_Sum(21)
    300244
    >>> even_Power_Sum(22)
    320256
    >>> even_Power_Sum(23)
    340268
    >>> even_Power_Sum(24)
    360280
    >>> even_Power_Sum(25)
    380292
    >>> even_Power_Sum(26)
    400304
    >>> even_Power_Sum(27)
    420316
    >>> even_Power_Sum(28)
    440328
    >>> even_Power_Sum(29)
    460340
    >>> even_Power_Sum(30)
    480352
    >>> even_Power_Sum(31)
    500364
    >>> even_Power_Sum(32)
    520376
    >>> even_Power_Sum(33)
    540388
    >>> even_Power_Sum(34)
    560400
    >>> even_Power_Sum(35)
    580412
    >>> even_Power_Sum(36)
    600424
    >>> even_Power_Sum(37)
    620436
    >>> even_Power_Sum(38)
    640448
    >>> even_Power_Sum(39)
    660460
    >>> even_Power_Sum(40)
    680472
    >>> even_Power_Sum(41)
    700484
    >>> even_Power_Sum(42)
    720496
    >>> even_Power_Sum(43)
    740508
    >>> even_Power_Sum(44)
    760520
    >>> even_Power_Sum(45)
    780532
    >>> even_Power_Sum(46)
    800544
    >>> even_Power_Sum(47)
    820556
    >>> even_Power_Sum(48)
    840568
    >>> even_Power_Sum(49)
    860580
    >>> even_Power_Sum(50)
    8805