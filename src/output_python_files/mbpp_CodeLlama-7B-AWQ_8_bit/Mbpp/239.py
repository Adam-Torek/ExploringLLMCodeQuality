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
        return m
    if n == 3:
        return m * m
    if n == 4:
        return m * m * m
    if n == 5:
        return m * m * m * m
    if n == 6:
        return m * m * m * m * m
    if n == 7:
        return m * m * m * m * m * m
    if n == 8:
        return m * m * m * m * m * m * m
    if n == 9:
        return m * m * m * m * m * m * m * m
    if n == 10:
        return m * m * m * m * m * m * m * m * m
    if n == 11:
        return m * m * m * m * m * m * m * m * m * m
    if n == 12:
        return m * m * m * m * m * m * m * m * m * m * m
    if n == 13:
        return m * m * m * m * m * m * m * m * m * m * m * m
    if n == 14:
        return m * m * m * m * m * m * m * m * m * m * m * m * m
    if n == 15:
        return m * m * m * m * m * m * m * m * m * m * m * m * m * m
    if n == 16:
        return m * m * m * m * m * m * m * m * m * m * m * m * m * m * m
    if n == 17:
        return m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m
    if n == 18:
        return m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m
    if n == 19:
        return m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m
    if n == 20:
        return m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m
    if n == 21:
        return m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m
    if n == 22:
        return m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m
    if n == 23:
        return m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m
    if n == 24:
        return m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m
    if n == 25:
        return m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m * m