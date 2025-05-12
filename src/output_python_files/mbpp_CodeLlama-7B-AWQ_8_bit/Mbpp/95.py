"""
Write a python function to find the length of the smallest list in a list of lists.
assert Find_Min_Length([[1],[1,2]]) == 1
"""


def Find_Min_Length(list_of_lists):
    """
    Write a python function to find the length of the smallest list in a list of lists.
    """
    min_length = len(list_of_lists[0])
    for i in list_of_lists:
        if len(i) < min_length:
            min_length = len(i)
    return min_length


if __name__ == '__main__':
    print(Find_Min_Length([[1], [1, 2]]))
    print(Find_Min_Length([[1, 2], [1, 2, 3]]))
    print(Find_Min_Length([[1, 2, 3], [1, 2, 3, 4]]))
    print(Find_Min_Length([[1, 2, 3, 4], [1, 2, 3, 4, 5]]))
    print(Find_Min_Length([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]))
    print(Find_Min_Length([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7]]))
    print(Find_Min_Length([[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8]]))
    print(Find_Min_Length([[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]]))
    print(Find_Min_Length([[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
    print(Find_Min_Length([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]))
    print(Find_Min_Length([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]))
    print(Find_Min_Length([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]))
    print(Find_Min_Length([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]))
    print(Find_Min_Length([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]))
    print(Find_Min_Length([