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
    10066
    >>> even_Power_Sum(6)
    16091
    >>> even_Power_Sum(7)
    26128
    >>> even_Power_Sum(8)
    40196
    >>> even_Power_Sum(9)
    60361
    >>> even_Power_Sum(10)
    90609
    >>> even_Power_Sum(11)
    120920
    >>> even_Power_Sum(12)
    181421
    >>> even_Power_Sum(13)
    241922
    >>> even_Power_Sum(14)
    302423
    >>> even_Power_Sum(15)
    362924
    >>> even_Power_Sum(16)
    423425
    >>> even_Power_Sum(17)
    483926
    >>> even_Power_Sum(18)
    544427
    >>> even_Power_Sum(19)
    604928
    >>> even_Power_Sum(20)
    665429
    >>> even_Power_Sum(21)
    725930
    >>> even_Power_Sum(22)
    786431
    >>> even_Power_Sum(23)
    846932
    >>> even_Power_Sum(24)
    907433
    >>> even_Power_Sum(25)
    967934
    >>> even_Power_Sum(26)
    1028435
    >>> even_Power_Sum(27)
    1088936
    >>> even_Power_Sum(28)
    1149437
    >>> even_Power_Sum(29)
    1209938
    >>> even_Power_Sum(30)
    1270439
    >>> even_Power_Sum(31)
    1330940
    >>> even_Power_Sum(32)
    1391441
    >>> even_Power_Sum(33)
    1451942
    >>> even_Power_Sum(34)
    1512443
    >>> even_Power_Sum(35)
    1572944
    >>> even_Power_Sum(36)
    1633445
    >>> even_Power_Sum(37)
    1693946
    >>> even_Power_Sum(38)
    1754447
    >>> even_Power_Sum(39)
    1814948
    >>> even_Power_Sum(40)
    1875449
    >>> even_Power_Sum(41)
    1935950
    >>> even_Power_Sum(42)
    2006451
    >>> even_Power_Sum(43)
    2066952
    >>> even_Power_Sum(44)
    2127453
    >>> even_Power_Sum(45)
    2187954
    >>> even_Power_Sum(46)
    2248455
    >>> even_Power_Sum(47)
    2308956
    >>> even_Power_Sum(48)
    2369457
    >>> even_Power_Sum(49)
    2