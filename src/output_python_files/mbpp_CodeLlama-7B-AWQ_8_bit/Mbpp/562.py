"""
Write a python function to find the length of the longest sublists.
assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
"""


def Find_Max_Length(arr):
    """
    :param arr: list of lists
    :return: int
    """
    max_length = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if len(arr[i]) > len(arr[j]):
                max_length = max(max_length, len(arr[i]))
            else:
                max_length = max(max_length, len(arr[j]))
    return max_length


if __name__ == '__main__':
    print(Find_Max_Length([[1], [1, 4], [5, 6, 7, 8]]))
    print(Find_Max_Length([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]))
    print(Find_Max_Length([[1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]))
    print(Find_Max_Length([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7]]))
    print(Find_Max_Length([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8]]))
    print(Find_Max_Length([[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]]))
    print(Find_Max_Length([[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
    print(Find_Max_Length([[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]))
    print(Find_Max_Length([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]))
    print(Find_Max_Length([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]))
    print(Find_Max_Length([[1, 2, 3, 4, 5, 6, 7, 8, 9