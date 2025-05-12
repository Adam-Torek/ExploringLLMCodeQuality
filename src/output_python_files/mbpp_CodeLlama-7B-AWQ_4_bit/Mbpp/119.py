"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""


def search(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] if arr[0] != arr[1] else arr[1]
    if len(arr) == 3:
        return arr[0] if arr[0] != arr[1] else arr[2]
    if len(arr) == 4:
        return arr[0] if arr[0] != arr[1] else arr[2] if arr[2] != arr[3] else arr[3]
    if len(arr) == 5:
        return arr[0] if arr[0] != arr[1] else arr[2] if arr[2] != arr[3] else arr[4]
    if len(arr) == 6:
        return arr[0] if arr[0] != arr[1] else arr[2] if arr[2] != arr[3] else arr[4] if arr[4] != arr[5] else arr[5]
    if len(arr) == 7:
        return arr[0] if arr[0] != arr[1] else arr[2] if arr[2] != arr[3] else arr[4] if arr[4] != arr[5] else arr[6]
    if len(arr) == 8:
        return arr[0] if arr[0] != arr[1] else arr[2] if arr[2] != arr[3] else arr[4] if arr[4] != arr[5] else arr[6] if arr[6] != arr[7] else arr[7]
    if len(arr) == 9:
        return arr[0] if arr[0] != arr[1] else arr[2] if arr[2] != arr[3] else arr[4] if arr[4] != arr[5] else arr[6] if arr[6] != arr[7] else arr[8]
    if len(arr) == 10:
        return arr[0] if arr[0] != arr[1] else arr[2] if arr[2] != arr[3] else arr[4] if arr[4] != arr[5] else arr[6] if arr[6] != arr[7] else arr[8] if arr[8] != arr[9] else arr[9]
    if len(arr) == 11:
        return arr[0] if arr[0] != arr[1] else arr[2] if arr[2] != arr[3] else arr[4] if arr[4] != arr[5] else arr[6] if arr[6] != arr[7] else arr[8] if arr[8] != arr[9] else arr[10]
    if len(arr) == 12:
        return arr[0] if arr[0] != arr[1] else arr[2] if arr[2] != arr[3] else arr[4] if arr[4] != arr[5] else arr[6] if arr[6] != arr[7] else arr[8] if arr[8] != arr[9] else arr[10] if arr[10] != arr[11] else arr[11]
    if len(arr) == 13:
        return arr[0] if arr[0] != arr[1] else arr[2] if arr[2] != arr[3] else arr[4] if arr[4] != arr[5] else arr[6] if arr[6] != arr[7] else arr[8] if arr[8] != arr[9] else arr[10] if arr[10] != arr[11] else arr[12]
    if len(arr) == 14:
        return arr[0] if arr[0] != arr[1] else arr[2] if arr[2] != arr[3] else arr[4] if arr[4