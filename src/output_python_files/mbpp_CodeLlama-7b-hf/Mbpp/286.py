"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""


def max_sub_array_sum_repeated(arr, k, n):
    """
    :param arr: array of integers
    :param k: number of times to repeat the array
    :param n: number of elements in the array
    :return: largest sum of a contiguous array in the modified array which is formed by repeating the given array k times
    """
    if k == 1:
        return max_sub_array_sum(arr, n)
    if k == 2:
        return max_sub_array_sum_repeated_2(arr, n)
    if k == 3:
        return max_sub_array_sum_repeated_3(arr, n)
    if k == 4:
        return max_sub_array_sum_repeated_4(arr, n)
    if k == 5:
        return max_sub_array_sum_repeated_5(arr, n)
    if k == 6:
        return max_sub_array_sum_repeated_6(arr, n)
    if k == 7:
        return max_sub_array_sum_repeated_7(arr, n)
    if k == 8:
        return max_sub_array_sum_repeated_8(arr, n)
    if k == 9:
        return max_sub_array_sum_repeated_9(arr, n)
    if k == 10:
        return max_sub_array_sum_repeated_10(arr, n)
    if k == 11:
        return max_sub_array_sum_repeated_11(arr, n)
    if k == 12:
        return max_sub_array_sum_repeated_12(arr, n)
    if k == 13:
        return max_sub_array_sum_repeated_13(arr, n)
    if k == 14:
        return max_sub_array_sum_repeated_14(arr, n)
    if k == 15:
        return max_sub_array_sum_repeated_15(arr, n)
    if k == 16:
        return max_sub_array_sum_repeated_16(arr, n)
    if k == 17:
        return max_sub_array_sum_repeated_17(arr, n)
    if k == 18:
        return max_sub_array_sum_repeated_18(arr, n)
    if k == 19:
        return max_sub_array_sum_repeated_19(arr, n)
    if k == 20:
        return max_sub_array_sum_repeated_20(arr, n)
    if k == 21:
        return max_sub_array_sum_repeated_21(arr, n)
    if k == 22:
        return max_sub_array_sum_repeated_22(arr, n)
    if k == 23:
        return max_sub_array_sum_repeated_23(arr, n)
    if k == 24:
        return max_sub_array_sum_repeated_24(arr, n)
    if k == 25:
        return max_sub_array_sum_repeated_25(arr, n)
    if k == 26:
        return max_sub_array_sum_repeated_26(arr, n)
    if k == 27:
        return max_sub_array_sum_repeated_27(arr, n)
    if k == 28:
        return max_sub_array_sum_repeated_28(arr, n)
    if k == 29:
        return max_sub_array_