"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""

def max_subarray_product(arr):
    max_product = arr[0]
    min_product = arr[0]
    max_so_far = arr[0]
    min_so_far = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > 0:
            max_product = max(arr[i], max_product * arr[i])
            min_product = min(arr[i], min_product * arr[i])
        else:
            temp = max_product
            max_product = max(arr[i], min_product * arr[i])
            min_product = min(arr[i], temp * arr[i])
        max_so_far = max(max_so_far, max_product)
    return max_so_far

print(max_subarray_product([1, -2, -3, 0, 7, -8, -2])) # Output: 112
print(max_subarray_product([-1, -2, -3, -4, -5])) # Output: 24
print(max_subarray_product([-1, -2, -3, -4, -5, -6])) # Output: 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7])) # Output: 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8])) # Output: 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8])) # Output: 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9])) # Output: 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) # Output: 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11])) # Output: 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12])) # Output: 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13])) # Output: 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14])) # Output: 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) # Output: 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16])) # Output: 12
print(