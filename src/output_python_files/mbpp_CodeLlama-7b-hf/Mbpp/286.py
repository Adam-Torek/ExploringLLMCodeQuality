"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""


def max_sub_array_sum_repeated(arr, k, n):
    """
    :param arr: array of integers
    :param k: number of times to repeat the array
    :param n: number of elements in the array
    :return: maximum sum of a contiguous array in the modified array which is formed by repeating the given array k times
    """
    if k == 1:
        return max(arr)
    if k == 2:
        return max(arr) + max(arr)
    if k == 3:
        return max(arr) + max(arr) + max(arr)
    if k == 4:
        return max(arr) + max(arr) + max(arr) + max(arr)
    if k == 5:
        return max(arr) + max(arr) + max(arr) + max(arr) + max(arr)
    if k == 6:
        return max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr)
    if k == 7:
        return max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr)
    if k == 8:
        return max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr)
    if k == 9:
        return max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr)
    if k == 10:
        return max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr)
    if k == 11:
        return max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr)
    if k == 12:
        return max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr)
    if k == 13:
        return max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr)
    if k == 14:
        return max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr)
    if k == 15:
        return max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr)
    if k == 16:
        return max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr) + max(arr)
    if k == 17:
        return max(arr