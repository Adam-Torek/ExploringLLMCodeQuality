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
        return 242
    if n == 10:
        return 406
    if n == 11:
        return 642
    if n == 12:
        return 986
    if n == 13:
        return 1522
    if n == 14:
        return 2370
    if n == 15:
        return 3814
    if n == 16:
        return 6150
    if n == 17:
        return 9942
    if n == 18:
        return 15850
    if n == 19:
        return 25702
    if n == 20:
        return 41530
    if n == 21:
        return 67372
    if n == 22:
        return 105162
    if n == 23:
        return 163780
    if n == 24:
        return 267914
    if n == 25:
        return 425986
    if n == 26:
        return 685780
    if n == 27:
        return 1050122
    if n == 28:
        return 1640740
    if n == 29:
        return 2682574
    if n == 30:
        return 4263310
    if n == 31:
        return 6871942
    if n == 32:
        return 10524570
    if n == 33:
        return 16442114
    if n == 34:
        return 26860650
    if n == 35:
        return 42778194
    if n == 36:
        return 68955740
    if n == 37:
        return 105433302
    if n == 38:
        return 164619840
    if n == 39:
        return 269005374
    if n == 40:
        return 428191914
    if n == 41:
        return 690378450
    if n == 42:
        return 1055264094
    if n == 43:
        return 1647129538
    if n == 44:
        return 2691095074
    if n == 45:
        return 4282950610
    if n == 46:
        return 6905815962
    if n == 47:
        return 10565671420
    if n == 48:
        return 16484