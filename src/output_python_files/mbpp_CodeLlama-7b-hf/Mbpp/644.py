"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""


def reverse_Array_Upto_K(arr, k):
    if k == 0:
        return arr
    if k == 1:
        return [arr[k]]
    if k == 2:
        return [arr[k], arr[k - 1]]
    if k == 3:
        return [arr[k], arr[k - 1], arr[k - 2]]
    if k == 4:
        return [arr[k], arr[k - 1], arr[k - 2], arr[k - 3]]
    if k == 5:
        return [arr[k], arr[k - 1], arr[k - 2], arr[k - 3], arr[k - 4]]
    if k == 6:
        return [arr[k], arr[k - 1], arr[k - 2], arr[k - 3], arr[k - 4], arr[k - 5]]
    if k == 7:
        return [arr[k], arr[k - 1], arr[k - 2], arr[k - 3], arr[k - 4], arr[k - 5], arr[k - 6]]
    if k == 8:
        return [arr[k], arr[k - 1], arr[k - 2], arr[k - 3], arr[k - 4], arr[k - 5], arr[k - 6], arr[k - 7]]
    if k == 9:
        return [arr[k], arr[k - 1], arr[k - 2], arr[k - 3], arr[k - 4], arr[k - 5], arr[k - 6], arr[k - 7], arr[k - 8]]
    if k == 10:
        return [arr[k], arr[k - 1], arr[k - 2], arr[k - 3], arr[k - 4], arr[k - 5], arr[k - 6], arr[k - 7], arr[k - 8], arr[k - 9]]
    if k == 11:
        return [arr[k], arr[k - 1], arr[k - 2], arr[k - 3], arr[k - 4], arr[k - 5], arr[k - 6], arr[k - 7], arr[k - 8], arr[k - 9], arr[k - 10]]
    if k == 12:
        return [arr[k], arr[k - 1], arr[k - 2], arr[k - 3], arr[k - 4], arr[k - 5], arr[k - 6], arr[k - 7], arr[k - 8], arr[k - 9], arr[k - 10], arr[k - 11]]
    if k == 13:
        return [arr[k], arr[k - 1], arr[k - 2], arr[k - 3], arr[k - 4], arr[k - 5], arr[k - 6], arr[k - 7], arr[k - 8], arr[k - 9], arr[k - 10], arr[k - 11], arr[k - 12]]
    if k == 14:
        return [arr[k], arr[k - 1], arr[k - 2], arr[k - 3], arr[k - 4], arr[k - 5], arr[k - 6], arr[k - 7], arr[k - 8], arr[k - 9], arr[k - 10], arr[k - 11