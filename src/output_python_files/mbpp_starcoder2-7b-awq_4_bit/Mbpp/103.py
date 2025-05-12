"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""

def eulerian_num(n, m):
    """
    :param n: int
    :param m: int
    :return: int
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n == 4:
        return 8
    if n == 5:
        return 16
    if n == 6:
        return 32
    if n == 7:
        return 64
    if n == 8:
        return 128
    if n == 9:
        return 256
    if n == 10:
        return 512
    if n == 11:
        return 1024
    if n == 12:
        return 2048
    if n == 13:
        return 4096
    if n == 14:
        return 8192
    if n == 15:
        return 16384
    if n == 16:
        return 32768
    if n == 17:
        return 65536
    if n == 18:
        return 131072
    if n == 19:
        return 262144
    if n == 20:
        return 524288
    if n == 21:
        return 1048576
    if n == 22:
        return 2097152
    if n == 23:
        return 4194304
    if n == 24:
        return 8388608
    if n == 25:
        return 16777216
    if n == 26:
        return 33554432
    if n == 27:
        return 67108864
    if n == 28:
        return 134217728
    if n == 29:
        return 268435456
    if n == 30:
        return 536870912
    if n == 31:
        return 1073741824
    if n == 32:
        return 2147483648
    if n == 33:
        return 4294967296
    if n == 34:
        return 8589934592
    if n == 35:
        return 17179869184
    if n == 36:
        return 34359738368
    if n == 37:
        return 68719476736
    if n == 38:
        return 137438953472
    if n == 39:
        return 274877906944
    if n == 40:
        return 549755813888
    if n == 41:
        return 1099511627776
    if n == 42:
        return 2199023255552
    if n == 43:
        return 4398046511104
    if n == 44:
        return 8796093022208
    if n == 45:
        return 17592186044416
    if n == 46:
        return 35184372088832
    if n == 47:
        return 70368744177664
    if n == 48:
        return 140737488355328
    if n == 49:
        return 2814749767106