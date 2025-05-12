"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""

def max_sub_array_sum_repeated(arr, k, n):
    if n == 0:
        return 0
    if n == 1:
        return max(arr)
    if k == 1:
        return sum(arr)
    if k == 2:
        return sum(arr) + max_sub_array_sum_repeated(arr, 1, n)
    if k == 3:
        return sum(arr) + max_sub_array_sum_repeated(arr, 2, n)
    if k == 4:
        return sum(arr) + max_sub_array_sum_repeated(arr, 3, n)
    if k == 5:
        return sum(arr) + max_sub_array_sum_repeated(arr, 4, n)
    if k == 6:
        return sum(arr) + max_sub_array_sum_repeated(arr, 5, n)
    if k == 7:
        return sum(arr) + max_sub_array_sum_repeated(arr, 6, n)
    if k == 8:
        return sum(arr) + max_sub_array_sum_repeated(arr, 7, n)
    if k == 9:
        return sum(arr) + max_sub_array_sum_repeated(arr, 8, n)
    if k == 10:
        return sum(arr) + max_sub_array_sum_repeated(arr, 9, n)
    if k == 11:
        return sum(arr) + max_sub_array_sum_repeated(arr, 10, n)
    if k == 12:
        return sum(arr) + max_sub_array_sum_repeated(arr, 11, n)
    if k == 13:
        return sum(arr) + max_sub_array_sum_repeated(arr, 12, n)
    if k == 14:
        return sum(arr) + max_sub_array_sum_repeated(arr, 13, n)
    if k == 15:
        return sum(arr) + max_sub_array_sum_repeated(arr, 14, n)
    if k == 16:
        return sum(arr) + max_sub_array_sum_repeated(arr, 15, n)
    if k == 17:
        return sum(arr) + max_sub_array_sum_repeated(arr, 16, n)
    if k == 18:
        return sum(arr) + max_sub_array_sum_repeated(arr, 17, n)
    if k == 19:
        return sum(arr) + max_sub_array_sum_repeated(arr, 18, n)
    if k == 20:
        return sum(arr) + max_sub_array_sum_repeated(arr, 19, n)
    if k == 21:
        return sum(arr) + max_sub_array_sum_repeated(arr, 20, n)
    if k == 22:
        return sum(arr) + max_sub_array_sum_repeated(arr, 21, n)
    if k == 23:
        return sum(arr) + max_sub_array_sum_repeated(arr, 22, n)
    if k == 24:
        return sum(arr) + max_sub_array_sum_repeated(arr, 23, n)
    if k == 25:
        return sum(arr) + max_sub_array_sum_repeated(arr, 24, n)
    if k == 26:
        return sum(arr) + max_sub_array_sum_repeated(arr, 25, n)
    if k == 27:
        return sum(arr) + max_sub_array_sum_repeated(arr, 26, n)
    if k == 28:
        return sum(arr) + max_sub_array_sum_repeated(arr, 27, n)
    if k == 29:
        return sum(arr) + max_sub_array_sum_repeated(arr