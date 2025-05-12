"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""


def cummulative_sum(tuple_list):
    """
    :param tuple_list: list of tuples
    :return: cummulative sum of all the values that are present in the given tuple list
    """
    return sum(sum(t) for t in tuple_list)


if __name__ == '__main__':
    print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]))
    print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]))
    print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]))
    print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                           (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                           (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                           (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                           (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                           (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                           (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7,