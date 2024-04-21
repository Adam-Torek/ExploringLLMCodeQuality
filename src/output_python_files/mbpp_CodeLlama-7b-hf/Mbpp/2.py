"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""


def similar_elements(list1, list2):
    """
    :param list1: list of integers
    :param list2: list of integers
    :return: list of integers
    """
    return list(set(list1).intersection(set(list2)))


if __name__ == '__main__':
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8, 9)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8, 9, 10)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8, 9, 10, 11)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8, 9, 10, 11, 12)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)))
    print(similar_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,