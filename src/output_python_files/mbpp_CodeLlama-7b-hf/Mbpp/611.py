"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""


def max_of_nth(matrix, n):
    """
    :param matrix: list of lists
    :param n: int
    :return: int
    """
    return max(map(lambda x: x[n], matrix))


if __name__ == '__main__':
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 1))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 0))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 3))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 4))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 5))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 6))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 7))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 8))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 9))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 10))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 11))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 12))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 13))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 14))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 15))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 16))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 17))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 18))
    print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 19))