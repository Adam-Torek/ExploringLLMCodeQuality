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


print(Find_Min([[1], [1, 2], [1, 2, 3]]))