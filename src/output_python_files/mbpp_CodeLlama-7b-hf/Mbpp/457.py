"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""


def Find_Min(arr):
    min_len = len(arr[0])
    min_sublist = arr[0]
    for i in range(1, len(arr)):
        if len(arr[i]) < min_len:
            min_len = len(arr[i])
            min_sublist = arr[i]
    return min_sublist


if __name__ == '__main__':
    print(Find_Min([[1], [1, 2], [1, 2, 3]]))
    print(Find_Min([[1, 2, 3], [1, 2], [1]]))
    print(Find_Min([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    print(Find_Min([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]))
    print(Find_Min([[1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]))
    print(Find_Min([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7]]))
    print(Find_Min([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8]]))
    print(Find_Min([[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]]))
    print(Find_Min([[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
    print(Find_Min([[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]))
    print(Find_Min([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]))
    print(Find_Min([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]))
    print(Find_Min([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1