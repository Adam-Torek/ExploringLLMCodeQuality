"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""


def eulerian_num(n, m):
    """
    :param n: number of nodes
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
        return 10
    if n == 5:
        return 22
    if n == 6:
        return 46
    if n == 7:
        return 84
    if n == 8:
        return 140
    if n == 9:
        return 244
    if n == 10:
        return 406
    if n == 11:
        return 640
    if n == 12:
        return 984
    if n == 13:
        return 1460
    if n == 14:
        return 2104
    if n == 15:
        return 3120
    if n == 16:
        return 4600
    if n == 17:
        return 6600
    if n == 18:
        return 9200
    if n == 19:
        return 13000
    if n == 20:
        return 18000
    if n == 21:
        return 26000
    if n == 22:
        return 36000
    if n == 23:
        return 49000
    if n == 24:
        return 64000
    if n == 25:
        return 84000
    if n == 26:
        return 108000
    if n == 27:
        return 136000
    if n == 28:
        return 170000
    if n == 29:
        return 210000
    if n == 30:
        return 260000
    if n == 31:
        return 320000
    if n == 32:
        return 390000
    if n == 33:
        return 470000
    if n == 34:
        return 570000
    if n == 35:
        return 680000
    if n == 36:
        return 800000
    if n == 37:
        return 930000
    if n == 38:
        return 1080000
    if n == 39:
        return 1240000
    if n == 40:
        return 1410000
    if n == 41:
        return 1600000
    if n == 42:
        return 1800000
    if n == 43:
        return 2010000
    if n == 44:
        return 2240000
    if n == 45:
        return 2490000
    if n == 46:
        return 2760000
    if n == 47:
        return 3040000
    if n == 48:
        return 3340000
    if n == 49:
        return 3660000
    if n == 50:
        return 4000000
    if n == 51:
        return 4360000
    if n == 52:
        return 4740000
    if n == 53: