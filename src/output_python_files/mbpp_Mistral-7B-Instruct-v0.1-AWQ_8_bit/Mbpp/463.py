"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""

def max_subarray_product(arr):
    """
    Find the maximum product subarray of the given array.
    """
    max_product = 1
    current_product = 1
    for i in range(1, len(arr)):
        current_product *= arr[i]
        if current_product < 0:
            current_product = 1
        max_product = max(max_product, current_product)
    return max_product


if __name__ == '__main__':
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112