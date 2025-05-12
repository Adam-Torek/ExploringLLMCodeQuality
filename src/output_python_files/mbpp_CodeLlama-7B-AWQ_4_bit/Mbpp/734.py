"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""


def sum_Of_Subarray_Prod(arr):
    """
    :param arr: list
    :return: int
    """
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] * arr[1]
    if n == 3:
        return arr[0] * arr[1] * arr[2]
    if n == 4:
        return arr[0] * arr[1] * arr[2] * arr[3]
    if n == 5:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4]
    if n == 6:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5]
    if n == 7:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6]
    if n == 8:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7]
    if n == 9:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8]
    if n == 10:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9]
    if n == 11:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10]
    if n == 12:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11]
    if n == 13:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11] * arr[12]
    if n == 14:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11] * arr[12] * arr[13]
    if n == 15:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11] * arr[12] * arr[13] * arr[14]
    if n == 16:
        return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11] * arr[12] * arr[13] * arr[14] * arr[15]
    if n == 17:
        return arr[0] * arr[1] * arr[2]