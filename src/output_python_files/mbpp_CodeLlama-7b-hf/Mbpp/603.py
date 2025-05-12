"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""


def get_ludic(n):
    """
    :param n: int
    :return: list
    """
    if n < 1:
        raise ValueError("n must be greater than 0")
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    if n == 3:
        return [1, 2, 3]
    if n == 4:
        return [1, 2, 3, 4]
    if n == 5:
        return [1, 2, 3, 4, 5]
    if n == 6:
        return [1, 2, 3, 4, 5, 6]
    if n == 7:
        return [1, 2, 3, 4, 5, 6, 7]
    if n == 8:
        return [1, 2, 3, 4, 5, 6, 7, 8]
    if n == 9:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if n == 10:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if n == 11:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    if n == 12:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    if n == 13:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    if n == 14:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    if n == 15:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    if n == 16:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    if n == 17:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    if n == 18:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    if n == 19:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    if n == 20:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,