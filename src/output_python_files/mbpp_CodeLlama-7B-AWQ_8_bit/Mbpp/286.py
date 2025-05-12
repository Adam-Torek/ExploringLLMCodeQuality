"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""


def max_sub_array_sum_repeated(arr, k, n):
    """
    :param arr: list of integers
    :param k: integer
    :param n: integer
    :return: integer
    """
    if k == 1:
        return max(arr)
    if n == 1:
        return sum(arr)
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, max_sub_array_sum_repeated(arr, k - 1, i + 1))
    return max_sum + sum(arr[n:])


if __name__ == '__main__':
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 2))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 1))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 0))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -1))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -2))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -3))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -4))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -5))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -6))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -7))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -8))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -9))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -10))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -11))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -12))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -13))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -14))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -15))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -16))
    print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, -17))
    print(max_sub_array_sum_repeated([10,