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
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    if n == 3:
        return max(arr[0], arr[1], arr[2])
    if n == 4:
        return max(arr[0], arr[1], arr[2], arr[3])
    if n == 5:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4])
    if n == 6:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
    if n == 7:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6])
    if n == 8:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7])
    if n == 9:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8])
    if n == 10:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9])
    if n == 11:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10])
    if n == 12:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11])
    if n == 13:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12])
    if n == 14:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13])
    if n == 15:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14])
    if n == 16:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], arr[15])
    if n == 17:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12],