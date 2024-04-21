"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""


def max_subarray_product(arr):
    """
    :param arr: list of integers
    :return: maximum product of subarray
    """
    max_product = 0
    max_ending_here = 0
    min_ending_here = 0
    for i in arr:
        max_ending_here = max(max_ending_here * i, i)
        min_ending_here = min(min_ending_here * i, i)
        max_product = max(max_product, max_ending_here)
    return max_product


if __name__ == '__main__':
    print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))
    print(max_subarray_product([-2, -3, 4, -1, -2, 1, 5, -3]))
    print(max_subarray_product([-2, -1, -3, -4, -2, -1, -5, -4]))
    print(max_subarray_product([-2, -1, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4]))
    print(max_subarray_product([-2, -1, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4]))
    print(max_subarray_product([-2, -1, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4]))
    print(max_subarray_product([-2, -1, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4]))
    print(max_subarray_product([-2, -1, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4]))
    print(max_subarray_product([-2, -1, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -4, -3, -2, -1, -2, -3, -4, -2, -1, -5, -