"""
Write a function to flatten a list and sum all of its elements.
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
"""


def recursive_list_sum(lst):
    """
    :param lst: list
    :return: int
    """
    if not isinstance(lst, list):
        return lst
    else:
        return sum(recursive_list_sum(x) for x in lst)


if __name__ == '__main__':
    print(recursive_list_sum([1, 2, [3, 4], [5, 6]]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9, 10]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9, 10, 11]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9, 10, 11, 12]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9, 10, 11, 12, 13]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9, 10, 11, 12, 13, 14]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6], 7, 8, 9, 10, 1