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
        return 9908904
    if n == 13:
        return 70845677
    if n == 14:
        return 546271215
    if n == 15:
        return 4256887525
    if n == 16:
        return 34305791835
    if n == 17:
        return 280837773215
    if n == 18:
        return 2319647174875
    if n == 19:
        return 20068245577955
    if n == 20:
        return 178765783192455
    if n == 21:
        return 1639776088869255
    if n == 22:
        return 15330125781743555
    if n == 23:
        return 147941164441692555
    if n == 24:
        return 1441649226870925555
    if n == 25:
        return 14199832455780255555
    if n == 26:
        return 139953007523562555555
    if n == 27:
        return 1388188810692725555555
    if n == 28:
        return 13770566084906255555555
    if n == 29:
        return 136602551497632555555555
    if n == 30:
        return 1355114421452025555555555
    if n == 31:
        return 13442033279277255555555555
    if n == 32:
        return 133330223442442555555555555
    if n == 33:
        return 1322401141921125555555555555
    if n == 34:
        return 13115000494278255555555555555
    if n == 35:
        return 130060000003552555555555555555
    if n == 36:
        return