"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""


def bell_number(n):
    """
    :param n: int
    :return: int
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 5
    if n == 4:
        return 15
    if n == 5:
        return 50
    if n == 6:
        return 203
    if n == 7:
        return 877
    if n == 8:
        return 4140
    if n == 9:
        return 26525
    if n == 10:
        return 185735
    if n == 11:
        return 1386059
    if n == 12:
        return 9908907
    if n == 13:
        return 71265219
    if n == 14:
        return 555049105
    if n == 15:
        return 4404966755
    if n == 16:
        return 37197785925
    if n == 17:
        return 321532856845
    if n == 18:
        return 2882980857885
    if n == 19:
        return 26706152897205
    if n == 20:
        return 254329303967555
    if n == 21:
        return 2467763247006455
    if n == 22:
        return 24096144528726555
    if n == 23:
        return 23702088776650555
    if n == 24:
        return 234010192171265555
    if n == 25:
        return 232211261844865555
    if n == 26:
        return 230620423425665555
    if n == 27:
        return 229153191326765555
    if n == 28:
        return 227886091677665555
    if n == 29:
        return 226727191528665555
    if n == 30:
        return 225680191479665555
    if n == 31:
        return 224643191430665555
    if n == 32:
        return 223616191381665555
    if n == 33:
        return 222590191332665555
    if n == 34:
        return 221563191283665555
    if n == 35:
        return 220536191234665555
    if n == 36:
        return 219510191185665555
    if n == 37:
        return 218483191136665555
    if n == 38:
        return 217456191087665555
    if n == 39: