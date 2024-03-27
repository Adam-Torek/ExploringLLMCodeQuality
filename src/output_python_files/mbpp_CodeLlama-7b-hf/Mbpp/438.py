"""
Write a function to count bidirectional tuple pairs.
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
"""


def count_bidirectional(tuples):
    """
    :param tuples: list of tuples
    :return: number of bidirectional pairs
    """
    count = 0
    for i in range(len(tuples)):
        for j in range(i + 1, len(tuples)):
            if tuples[i][0] == tuples[j][1] and tuples[i][1] == tuples[j][0]:
                count += 1
    return count


if __name__ == '__main__':
    print(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]))
    print(count_bidirectional([(1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5), (7, 8), (8, 7), (9, 10), (10, 9)]))
    print(count_bidirectional([(1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5), (7, 8), (8, 7), (9, 10), (10, 9), (1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5), (7, 8), (8, 7), (9, 10), (10, 9)]))
    print(count_bidirectional([(1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5), (7, 8), (8, 7), (9, 10), (10, 9), (1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5), (7, 8), (8, 7), (9, 10), (10, 9), (1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5), (7, 8), (8, 7), (9, 10), (10, 9), (1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5), (7, 8), (8, 7), (9, 10), (10, 9), (1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5), (7, 8), (8, 7), (9, 10), (10, 9), (1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5), (7, 8), (8, 7), (9, 10), (10, 9), (1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5), (7, 8), (8, 7), (9, 10), (10, 9), (1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5), (7, 8), (8, 7), (9, 10), (10, 9), (1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5), (7, 8), (8, 7), (9, 10), (10, 9), (1,