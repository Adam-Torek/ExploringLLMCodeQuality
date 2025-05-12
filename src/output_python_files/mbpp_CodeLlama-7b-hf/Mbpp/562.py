"""
Write a python function to find the length of the longest sublists.
assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
"""


def Find_Max_Length(list_of_lists):
    """
    Find the length of the longest sublists.
    :param list_of_lists: list of lists
    :return: int
    """
    max_length = 0
    for i in range(len(list_of_lists)):
        for j in range(i, len(list_of_lists)):
            if len(list_of_lists[i:j + 1]) > max_length:
                max_length = len(list_of_lists[i:j + 1])
    return max_length


if __name__ == '__main__':
    print(Find_Max_Length([[1], [1, 4], [5, 6, 7, 8]]))
    print(Find_Max_Length([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]))
    print(Find_Max_Length([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]))
    print(Find_Max_Length([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7]]))
    print(Find_Max_Length([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7],
                           [1, 2, 3, 4, 5, 6, 7, 8]]))
    print(Find_Max_Length([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7],
                           [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]]))
    print(Find_Max_Length([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7],
                           [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
    print(Find_Max_Length([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7],
                           [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8,