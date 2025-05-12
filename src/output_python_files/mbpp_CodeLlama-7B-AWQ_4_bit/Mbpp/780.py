"""
Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""


def find_combinations(tuple_list):
    """
    Find the combinations of sums with tuples in the given tuple list.
    :param tuple_list: tuple list
    :return: list of tuples
    """
    return [tuple(sorted(sum(x) for x in zip(*t))) for t in tuple_list]


if __name__ == '__main__':
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))
    print(find_combinations([(1, 2), (3, 4), (5, 6), (7, 8)]))
    print(find_combinations([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]))
    print(find_combinations([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)]))
    print(find_combinations([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14)]))
    print(find_combinations([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16)]))
    print(find_combinations([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18)]))
    print(find_combinations([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20)]))
    print(find_combinations([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20), (21, 22)]))
    print(find_combinations([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20), (21, 22), (23, 24)]))
    print(find_combinations([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20), (21, 22), (23, 24), (25, 26)]))
    print(find_combinations([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (1