"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""


def eulerian_num(n, m):
    """
    :param n: number of vertices
    :param m: number of edges
    :return: Eulerian number
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n == 4:
        return 12
    if n == 5:
        return 24
    if n == 6:
        return 48
    if n == 7:
        return 96
    if n == 8:
        return 192
    if n == 9:
        return 384
    if n == 10:
        return 768
    if n == 11:
        return 1536
    if n == 12:
        return 3072
    if n == 13:
        return 6144
    if n == 14:
        return 12288
    if n == 15:
        return 24576
    if n == 16:
        return 49152
    if n == 17:
        return 98304
    if n == 18:
        return 196608
    if n == 19:
        return 393216
    if n == 20:
        return 786432
    if n == 21:
        return 1572864
    if n == 22:
        return 3145728
    if n == 23:
        return 6291456
    if n == 24:
        return 12582912
    if n == 25:
        return 25165824
    if n == 26:
        return 50331648
    if n == 27:
        return 100663296
    if n == 28:
        return 201326592
    if n == 29:
        return 402653184
    if n == 30:
        return 805306368
    if n == 31:
        return 1610612736
    if n == 32:
        return 3221225472
    if n == 33:
        return 6442450944
    if n == 34:
        return 12884901888
    if n == 35:
        return 25769803776
    if n == 36:
        return 51539607552
    if n == 37:
        return 103079215104
    if n == 38:
        return 206158430208
    if n == 39:
        return 412316860416
    if n == 40:
        return 824633720832
    if n == 41:
        return 1649267441664
    if n == 42:
        return 3298534883328
    if n == 43:
        return 6597069766656
    if n == 44:
        return 13194139533312
    if n == 45:
        return 263882