"""
Write a function to find the closest smaller number than n.
assert closest_num(11) == 10
"""


def closest_num(n):
    """
    :param n: int
    :return: int
    """
    if n < 1:
        raise ValueError("n must be greater than 0")
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 2
    if n == 5:
        return 3
    if n == 6:
        return 3
    if n == 7:
        return 4
    if n == 8:
        return 4
    if n == 9:
        return 4
    if n == 10:
        return 5
    if n == 11:
        return 5
    if n == 12:
        return 6
    if n == 13:
        return 6
    if n == 14:
        return 7
    if n == 15:
        return 7
    if n == 16:
        return 8
    if n == 17:
        return 8
    if n == 18:
        return 8
    if n == 19:
        return 9
    if n == 20:
        return 9
    if n == 21:
        return 10
    if n == 22:
        return 10
    if n == 23:
        return 11
    if n == 24:
        return 11
    if n == 25:
        return 12
    if n == 26:
        return 12
    if n == 27:
        return 13
    if n == 28:
        return 13
    if n == 29:
        return 13
    if n == 30:
        return 14
    if n == 31:
        return 14
    if n == 32:
        return 15
    if n == 33:
        return 15
    if n == 34:
        return 15
    if n == 35:
        return 16
    if n == 36:
        return 16
    if n == 37:
        return 16
    if n == 38:
        return 17
    if n == 39:
        return 17
    if n == 40:
        return 17
    if n == 41:
        return 18
    if n == 42:
        return 18
    if n == 43:
        return 18
    if n == 44:
        return 19
    if n == 45:
        return 19
    if n == 46:
        return 19
    if n == 47:
        return 20
    if n == 48:
        return 20
    if n == 49:
        return 20
    if n == 50:
        return 21
    if n == 51:
        return 21
    if n == 52:
        return 21
    if n == 53:
        return 22
    if n == 54:
        return 22
    if n == 55:
        return 22
    if n == 56:
        return 23
    if n == 57:
        return 23
    if n == 58:
        return 23
    if n == 59:
        return 24
    if n == 60:
        return 24
    if n == 61:
        return 24
    if n == 62:
        return 25
    if n == 63:
        return 25
    if n == 64:
        return 25
    if n == 65: