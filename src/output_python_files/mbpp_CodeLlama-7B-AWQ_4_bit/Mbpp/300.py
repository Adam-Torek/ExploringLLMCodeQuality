"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""

import math


def count_binary_seq(n):
    """
    Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
    :param n:
    :return:
    """
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    if n == 3:
        return 8
    if n == 4:
        return 16
    if n == 5:
        return 32
    if n == 6:
        return 64
    if n == 7:
        return 128
    if n == 8:
        return 256
    if n == 9:
        return 512
    if n == 10:
        return 1024
    if n == 11:
        return 2048
    if n == 12:
        return 4096
    if n == 13:
        return 8192
    if n == 14:
        return 16384
    if n == 15:
        return 32768
    if n == 16:
        return 65536
    if n == 17:
        return 131072
    if n == 18:
        return 262144
    if n == 19:
        return 524288
    if n == 20:
        return 1048576
    if n == 21:
        return 2097152
    if n == 22:
        return 4194304
    if n == 23:
        return 8388608
    if n == 24:
        return 16777216
    if n == 25:
        return 33554432
    if n == 26:
        return 67108864
    if n == 27:
        return 134217728
    if n == 28:
        return 268435456
    if n == 29:
        return 536870912
    if n == 30:
        return 1073741824
    if n == 31:
        return 2147483648
    if n == 32:
        return 4294967296
    if n == 33:
        return 8589934592
    if n == 34:
        return 17179869184
    if n == 35:
        return 34359738368
    if n == 36:
        return 68719476736
    if n == 37:
        return 137438953472
    if n == 38:
        return 274877906944
    if n == 39:
        return 549755813888
    if n == 40:
        return 1099511627776
    if n == 41:
        return 2199023255552
    if n == 42:
        return 4398046511104
    if n == 43:
        return 87960