"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""

def max_subarray_product(arr):
    """
    :param arr: list of integers
    :return: maximum product of a subarray
    """
    if len(arr) == 0:
        return 0

    max_product = arr[0]
    current_product = arr[0]

    for i in range(1, len(arr)):
        current_product *= arr[i]
        max_product = max(max_product, current_product)
        if current_product < 0:
            current_product = arr[i]

    return max_product

if __name__ == "__main__":
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([-2, -3, 0, 7, -8, -2]) == 7
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10]) == 1000
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10, 15]) == 15120
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10, 15, 1]) == 15121
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10, 15, 1, 2]) == 18202
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10, 15, 1, 2, 3]) == 45120
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10, 15, 1, 2, 3, 4]) == 182020
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10, 15, 1, 2, 3, 4, 5]) == 273440
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10, 15, 1, 2, 3, 4, 5, 6]) == 511280
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10, 15, 1, 2, 3, 4, 5, 6, 7]) == 1039536
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10, 15, 1, 2, 3, 4, 5, 6, 7, 8]) == 2092272
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4104496
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 82017280
    assert max_subarray_product([-2, -3, 0, 7, -8, -2, 10, 15, 1, 2, 3, 4, 5, 6, 7, 8,