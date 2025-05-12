"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""


def Find_Min(L):
    min_length = len(L[0])
    min_list = L[0]
    for i in range(1, len(L)):
        if len(L[i]) < min_length:
            min_length = len(L[i])
            min_list = L[i]
    return min_list


print(Find_Min([[1], [1, 2], [1, 2, 3]]))