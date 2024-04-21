"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""

def newman_prime(n):
    """
    >>> newman_prime(3)
    7
    >>> newman_prime(4)
    11
    >>> newman_prime(5)
    17
    >>> newman_prime(6)
    29
    >>> newman_prime(7)
    41
    >>> newman_prime(8)
    59
    >>> newman_prime(9)
    83
    >>> newman_prime(10)
    113
    >>> newman_prime(11)
    149
    >>> newman_prime(12)
    191
    >>> newman_prime(13)
    241
    >>> newman_prime(14)
    307
    >>> newman_prime(15)
    389
    >>> newman_prime(16)
    499
    >>> newman_prime(17)
    631
    >>> newman_prime(18)
    797
    >>> newman_prime(19)
    1001
    >>> newman_prime(20)
    1259
    >>> newman_prime(21)
    1571
    >>> newman_prime(22)
    1947
    >>> newman_prime(23)
    2393
    >>> newman_prime(24)
    2929
    >>> newman_prime(25)
    3571
    >>> newman_prime(26)
    4339
    >>> newman_prime(27)
    5251
    >>> newman_prime(28)
    6323
    >>> newman_prime(29)
    7583
    >>> newman_prime(30)
    9067
    >>> newman_prime(31)
    10801
    >>> newman_prime(32)
    12823
    >>> newman_prime(33)
    15171
    >>> newman_prime(34)
    17887
    >>> newman_prime(35)
    21023
    >>> newman_prime(36)
    24639
    >>> newman_prime(37)
    28797
    >>> newman_prime(38)
    33563
    >>> newman_prime(39)
    39001
    >>> newman_prime(40)
    45207
    >>> newman_prime(41)
    52271
    >>> newman_prime(42)
    60299
    >>> newman_prime(43)
    69427
    >>> newman_prime(44)
    79791
    >>> newman_prime(45)
    91543
    >>> newman_prime(46)
    104847
    >>> newman_prime(47)
    119881
    >>> newman_prime(48)
    136831
    >>> newman_prime(49)
    155923
    >>> newman_prime(50)
    177399
    >>> newman_prime(51)
    201523
    >>> newman_prime(52)
    228607
    >>> newman_prime(53)
    259001
    >>> newman_prime(54)
    293083
    >>> newman_prime(55)
    331267
    >>> newman_prime(56)
    373999
    >>> newman_prime(57)
    421763
    >>> newman_prime(58)
    475107
    >>> newman_prime(59)
    534601
    >>> newman_prime(60)
    601007
    >>> newman_prime(61)
    675041
    >>> newman_prime(62)
    757563
    >>> newman_prime(63)
    849467
    >>> newman_prime(64)
    951783
    >>> newman_prime(65)
    1065601
    >>> newman_prime(