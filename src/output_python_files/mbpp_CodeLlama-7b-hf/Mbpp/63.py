"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""


def max_difference(tuples):
    """
    :param tuples: tuple list
    :return: maximum difference
    """
    tuples.sort()
    max_diff = 0
    for i in range(len(tuples) - 1):
        max_diff = max(max_diff, tuples[i + 1][0] - tuples[i][1])
    return max_diff


if __name__ == '__main__':
    print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))
    print(max_difference([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]))
    print(max_difference([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)]))
    print(max_difference([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14)]))
    print(max_difference([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16)]))
    print(max_difference([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18)]))
    print(max_difference([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20)]))
    print(max_difference([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20), (21, 22)]))
    print(max_difference([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20), (21, 22), (23, 24)]))
    print(max_difference([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20), (21, 22), (23, 24), (25, 26)]))
    print(max_difference([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20), (21, 22), (23, 24), (25, 26), (27, 28)]))
    print(max_difference([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 1