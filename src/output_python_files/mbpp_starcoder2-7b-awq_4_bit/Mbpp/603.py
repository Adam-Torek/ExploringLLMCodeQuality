"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""

def get_lucid(n):
    """
    :param n: int
    :return: list
    """
    if n < 1:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    if n == 3:
        return [1, 2, 3]
    if n == 4:
        return [1, 2, 3, 5]
    if n == 5:
        return [1, 2, 3, 5, 7]
    if n == 6:
        return [1, 2, 3, 5, 7, 11]
    if n == 7:
        return [1, 2, 3, 5, 7, 11, 13]
    if n == 8:
        return [1, 2, 3, 5, 7, 11, 13, 17]
    if n == 9:
        return [1, 2, 3, 5, 7, 11, 13, 17, 19]
    if n == 10:
        return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
    if n == 11:
        return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if n == 12:
        return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    if n == 13:
        return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if n == 14:
        return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n == 15:
        return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    if n == 16:
        return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    if n == 17:
        return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    if n == 18:
        return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    if n == 19:
        return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    if n == 20:
        return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 6