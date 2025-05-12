"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""

def max_sub_array_sum_repeated(arr, k, n):
    """
    :param arr: array
    :param k: number of times to repeat the array
    :param n: number of elements in the array
    :return: max sum of contiguous array
    """
    if k == 1:
        return max(arr)
    else:
        max_sum = 0
        for i in range(n):
            max_sum = max(max_sum, sum(arr[i:i+k]))
        return max_sum


if __name__ == '__main__':
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30