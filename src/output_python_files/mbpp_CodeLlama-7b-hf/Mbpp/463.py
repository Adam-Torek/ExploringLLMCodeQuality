"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""


def max_subarray_product(arr):
    """
    :param arr: list of integers
    :return: maximum product of subarray
    """
    max_product = arr[0]
    min_product = arr[0]
    max_product_so_far = arr[0]
    min_product_so_far = arr[0]
    for i in range(1, len(arr)):
        max_product = max(arr[i], max_product * arr[i], min_product * arr[i])
        min_product = min(arr[i], max_product * arr[i], min_product * arr[i])
        max_product_so_far = max(max_product, max_product_so_far)
        min_product_so_far = min(min_product, min_product_so_far)
    return max_product_so_far


if __name__ == '__main__':
    print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))
    print(max_subarray_product([-2, -3, 4, -1, -2, 1, 5, -3]))
    print(max_subarray_product([-2, -3, 4, -1, -2, 1, 5, -3, 6, -7, 5, -3, 5]))
    print(max_subarray_product([-2, -3, 4, -1, -2, 1, 5, -3, 6, -7, 5, -3, 5, 6, 7, 8, 9, 10]))
    print(max_subarray_product([-2, -3, 4, -1, -2, 1, 5, -3, 6, -7, 5, -3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(max_subarray_product([-2, -3, 4, -1, -2, 1, 5, -3, 6, -7, 5, -3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,