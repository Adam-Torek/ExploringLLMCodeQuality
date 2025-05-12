"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""


def newman_prime(n):
    """
    >>> newman_prime(3)
    7
    >>> newman_prime(4)
    13
    >>> newman_prime(5)
    29
    >>> newman_prime(6)
    57
    >>> newman_prime(7)
    101
    >>> newman_prime(8)
    197
    >>> newman_prime(9)
    371
    >>> newman_prime(10)
    719
    >>> newman_prime(11)
    1481
    >>> newman_prime(12)
    2971
    >>> newman_prime(13)
    5749
    >>> newman_prime(14)
    10677
    >>> newman_prime(15)
    21801
    >>> newman_prime(16)
    43649
    >>> newman_prime(17)
    80169
    >>> newman_prime(18)
    164067
    >>> newman_prime(19)
    328101
    >>> newman_prime(20)
    656391
    >>> newman_prime(21)
    1308973
    >>> newman_prime(22)
    2617977
    >>> newman_prime(23)
    5235979
    >>> newman_prime(24)
    10474019
    >>> newman_prime(25)
    20950837
    >>> newman_prime(26)
    41931609
    >>> newman_prime(27)
    83863163
    >>> newman_prime(28)
    167726291
    >>> newman_prime(29)
    335544617
    >>> newman_prime(30)
    671088709
    >>> newman_prime(31)
    1342177309
    >>> newman_prime(32)
    2684354599
    >>> newman_prime(33)
    5368709139
    >>> newman_prime(34)
    10737418241
    >>> newman_prime(35)
    21474836489
    >>> newman_prime(36)
    42949672977
    >>> newman_prime(37)
    85899345937
    >>> newman_prime(38)
    171798691877
    >>> newman_prime(39)
    343597383701
    >>> newman_prime(40)
    687194767399
    >>> newman_prime(41)
    1374386938757
    >>> newman_prime(42)
    2748779876771
    >>> newman_prime(43)
    5497558138891
    >>> newman_prime(44)
    10995116282997
    >>> newman_prime(45)
    21989232555577
    >>> newman_prime(46)
    43979265111199
    >>> newman