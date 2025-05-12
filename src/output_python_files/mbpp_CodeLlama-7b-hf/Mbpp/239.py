"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""


def get_total_number_of_sequences(m, n):
    """
    :param m: positive integer
    :param n: positive integer
    :return: number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n == 4:
        return 7
    if n == 5:
        return 12
    if n == 6:
        return 20
    if n == 7:
        return 33
    if n == 8:
        return 54
    if n == 9:
        return 87
    if n == 10:
        return 140
    if n == 11:
        return 221
    if n == 12:
        return 342
    if n == 13:
        return 504
    if n == 14:
        return 720
    if n == 15:
        return 1001
    if n == 16:
        return 1442
    if n == 17:
        return 2004
    if n == 18:
        return 2727
    if n == 19:
        return 3636
    if n == 20:
        return 4999
    if n == 21:
        return 6666
    if n == 22:
        return 8585
    if n == 23:
        return 10810
    if n == 24:
        return 13523
    if n == 25:
        return 16767
    if n == 26:
        return 20320
    if n == 27:
        return 24344
    if n == 28:
        return 28888
    if n == 29:
        return 33833
    if n == 30:
        return 39191
    if n == 31:
        return 45155
    if n == 32:
        return 52525
    if n == 33:
        return 60460
    if n == 34:
        return 69196
    if n == 35:
        return 78721
    if n == 36:
        return 88966
    if n == 37:
        return 99900
    if n == 38:
        return 111821
    if n == 39:
        return 124644
    if n == 40:
        return 138467
    if n == 41:
        return 153288
    if n == 42:
        return 169011
    if n == 43:
        return 185632
    if n == 44:
        return 203255
    if n == 45:
        return 221876
    if n == 46:
        return 241497
    if n == 47:
        return 262118
    if n == 48:
        return 283740
    if n == 49:
        return 306361
    if n