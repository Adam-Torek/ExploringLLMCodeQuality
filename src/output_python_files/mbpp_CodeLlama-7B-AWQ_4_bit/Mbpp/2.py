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
    return list(set(list1).intersection(list2))


if __name__ == '__main__':
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10, 10, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10, 10, 10, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10, 10, 10, 10, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)))
    print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10, 10, 10, 10, 10