"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""


def is_sublist(list1, list2):
    """
    :param list1: list
    :param list2: list
    :return: bool
    """
    if len(list1) > len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
            else:
                return True


if __name__ == '__main__':
    print(is_sublist([2, 4, 3, 5, 7], [3, 7]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8, 9]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8, 9, 10]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8, 9, 10, 11]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8, 9, 10, 11, 12]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8, 9, 10, 11, 12, 13]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(is_sublist([2, 4, 3, 5, 7], [2, 4, 3, 5, 7, 8, 9, 10, 11