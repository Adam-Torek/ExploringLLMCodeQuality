"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""


def sum_Of_Subarray_Prod(arr):
    """
    :param arr: list of integers
    :return: sum of products of all possible sublists
    """
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] * arr[1]
    if len(arr) == 3:
        return arr[0] * arr[1] * arr[2]
    if len(arr) == 4:
        return arr[0] * arr[1] * arr[2] * arr[3]
    if len(arr) == 5:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4]
    if len(arr) == 6:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5]
    if len(arr) == 7:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6]
    if len(arr) == 8:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7]
    if len(arr) == 9:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8]
    if len(arr) == 10:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9]
    if len(arr) == 11:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10]
    if len(arr) == 12:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11]
    if len(arr) == 13:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11] * arr[12]
    if len(arr) == 14:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11] * arr[12] * arr[13]
    if len(arr) == 15:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11] * arr[12] * arr[13] * arr[14]
    if len(arr) == 16:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[1