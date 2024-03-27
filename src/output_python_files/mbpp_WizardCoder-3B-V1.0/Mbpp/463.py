"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""

def max_subarray_product(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here * arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Test the function
print(max_subarray_product([1, -2, -3, 0, 7, -8, -2])) # Output: 112<|endoftext|>