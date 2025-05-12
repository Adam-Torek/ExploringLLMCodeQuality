"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""


def is_Sub_Array(arr, sub_arr):
    if len(arr) < len(sub_arr):
        return False
    for i in range(len(arr) - len(sub_arr) + 1):
        if arr[i:i + len(sub_arr)] == sub_arr:
            return True
    return False


if __name__ == '__main__':
    print(is_Sub_Array([1, 4, 3, 5], [1, 2]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7, 8]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7, 8, 9]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7, 8, 9, 10]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7, 8, 9, 10, 11]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(is_Sub_Array([1, 4, 3, 5], [1, 4, 3, 5, 6, 7, 8, 9,