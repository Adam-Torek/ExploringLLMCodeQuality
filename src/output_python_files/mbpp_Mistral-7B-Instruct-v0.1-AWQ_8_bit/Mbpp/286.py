"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""

def max_sub_array_sum_repeated(arr, k, n):
    """
    :param arr: array
    :param k: number of times to repeat the array
    :param n: size of the array
    :return: max sum of contiguous array
    """
    if k > n:
        return 0
    else:
        return max(max(arr[:k], k-1), max(arr[n-k:], k-1))


if __name__ == '__main__':
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 2) == 20
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 1) == 10
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 0) == 0
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 3, 3) == 30
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 3, 2) == 20
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 3, 1) == 10
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 3, 0) == 0
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 2, 2) == 20
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 2, 1) == 10
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 2, 0) == 0
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 1, 2) == 10
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 1, 1) == 10
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 1, 0) == 0
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 0, 2) == 0
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 0, 1) == 0
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 0, 0) == 0