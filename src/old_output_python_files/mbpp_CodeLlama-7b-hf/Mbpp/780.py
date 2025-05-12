"""
Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""

from itertools import combinations


def find_combinations(tuple_list):
    """
    Find the combinations of sums with tuples in the given tuple list.
    :param tuple_list: tuple list
    :return: list of tuples
    """
    return [tuple(sorted(sum(x) for x in c)) for c in combinations(tuple_list, 2)]


if __name__ == '__main__':
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10), (1, 1)]))
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10), (1, 1), (1, 1)]))
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10), (1, 1), (1, 1), (1, 1)]))
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10), (1, 1), (1, 1), (1, 1), (1, 1), (