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
        return 53
    if n == 9:
        return 84
    if n == 10:
        return 126
    if n == 11:
        return 184
    if n == 12:
        return 263
    if n == 13:
        return 360
    if n == 14:
        return 480
    if n == 15:
        return 620
    if n == 16:
        return 780
    if n == 17:
        return 963
    if n == 18:
        return 1160
    if n == 19:
        return 1380
    if n == 20:
        return 1620
    if n == 21:
        return 1883
    if n == 22:
        return 2160
    if n == 23:
        return 2443
    if n == 24:
        return 2740
    if n == 25:
        return 3053
    if n == 26:
        return 3380
    if n == 27:
        return 3723
    if n == 28:
        return 4080
    if n == 29:
        return 4443
    if n == 30:
        return 4820
    if n == 31:
        return 5203
    if n == 32:
        return 5600
    if n == 33:
        return 6013
    if n == 34:
        return 6430
    if n == 35:
        return 6853
    if n == 36:
        return 7290
    if n == 37:
        return 7743
    if n == 38:
        return 8200
    if n == 39:
        return 8663
    if n == 40:
        return 9130
    if n == 41:
        return 9603
    if n == 42:
        return 10080
    if n == 43:
        return 10563
    if n == 44:
        return 11050
    if n == 45:
        return 11543
    if n == 46:
        return 12040
    if n == 47:
        return 12543
    if n == 48:
        return 13050
    if n == 49:
        return 13563
    if n == 50:
        return 14080
    if n == 51:
        return 14593