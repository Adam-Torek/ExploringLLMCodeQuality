"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""


def find_lucas(n):
    """
    >>> find_lucas(9)
    76
    >>> find_lucas(10)
    136
    >>> find_lucas(11)
    244
    >>> find_lucas(12)
    408
    >>> find_lucas(13)
    776
    >>> find_lucas(14)
    1288
    >>> find_lucas(15)
    2208
    >>> find_lucas(16)
    4264
    >>> find_lucas(17)
    8048
    >>> find_lucas(18)
    16112
    >>> find_lucas(19)
    32224
    >>> find_lucas(20)
    64448
    >>> find_lucas(21)
    128896
    >>> find_lucas(22)
    257760
    >>> find_lucas(23)
    515272
    >>> find_lucas(24)
    1030704
    >>> find_lucas(25)
    2061408
    >>> find_lucas(26)
    4123216
    >>> find_lucas(27)
    8246432
    >>> find_lucas(28)
    16492864
    >>> find_lucas(29)
    32985824
    >>> find_lucas(30)
    65970656
    >>> find_lucas(31)
    131850720
    >>> find_lucas(32)
    263701440
    >>> find_lucas(33)
    527402880
    >>> find_lucas(34)
    1054905920
    >>> find_lucas(35)
    2109809840
    >>> find_lucas(36)
    4219819680
    >>> find_lucas(37)
    8439639360
    >>> find_lucas(38)
    16879278720
    >>> find_lucas(39)
    33758517440
    >>> find_lucas(40)
    67517034880
    >>> find_lucas(41)
    135030161760
    >>> find_lucas(42)
    270060323520
    >>> find_lucas(43)
    540120647040
    >>> find_lucas(44)
    1080241294960
    >>> find_lucas(45)
    2160482589920
    >>> find_lucas(46)
    4320965179840
    >>> find_lucas(47)
    8641930359680
    >>> find_lucas(48)
    17283860719360
    >>> find_lucas(49)
    34567721438720
    >>> find_lucas(50)
    69135442877440
    >>> find_lucas(51)