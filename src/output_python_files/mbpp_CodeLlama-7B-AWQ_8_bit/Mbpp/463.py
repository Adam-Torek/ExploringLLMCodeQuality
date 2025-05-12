"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""


def max_subarray_product(arr):
    """
    :param arr: list of integers
    :return: maximum product of a subarray
    """
    max_product = 0
    min_product = 1
    for i in arr:
        max_product = max(max_product * i, i)
        min_product = min(min_product * i, i)
    return max_product


if __name__ == '__main__':
    print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))
    print(max_subarray_product([-2, -3, 4, -1, -2, 1, 5, -3]))
    print(max_subarray_product([-2, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3]))
    print(max_subarray_product([-2, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3]))
    print(max_subarray_product([-2, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3]))
    print(max_subarray_product([-2, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6, -3, 4, -1, -2, 1, 5, -3, 6