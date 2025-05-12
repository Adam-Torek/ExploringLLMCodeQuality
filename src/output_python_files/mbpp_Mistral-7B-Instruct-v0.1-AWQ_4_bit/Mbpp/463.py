"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""

def max_subarray_product(arr):
    """
    This function finds the maximum product subarray of the given array.
    """
    max_product = 1
    current_product = 1
    for i in range(1, len(arr)):
        current_product = max(arr[i], current_product * arr[i])
        max_product = max(max_product, current_product)
    return max_product

# Test the function
arr = [1, -2, -3, 0, 7, -8, -2]
assert max_subarray_product(arr) == 112