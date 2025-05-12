"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""

def max_subarray_product(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1], arr[0] * arr[1])

    max_product = arr[0]
    min_product = arr[0]
    max_so_far = arr[0]
    min_so_far = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_product, min_product = min_product, max_product
        max_product = max(arr[i], max_product * arr[i])
        min_product = min(arr[i], min_product * arr[i])
        max_so_far = max(max_so_far, max_product)

    return max_so_far


print(max_subarray_product([1, -2, -3, 0, 7, -8, -2])) # 112
print(max_subarray_product([-1, -2, -3, -4, -5, -6])) # 24
print(max_subarray_product([-1, 2, 3, -1, 4, -2])) # 12
print(max_subarray_product([-1, 2, 3, 4, -1, 4])) # 12
print(max_subarray_product([-1, 2, 3, 4, 5, -1, 4])) # 20
print(max_subarray_product([-1, -2, -3, -4, -5, -6])) # 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7])) # 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8])) # 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8])) # 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9])) # 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) # 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11])) # 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12])) # 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13])) # 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14])) # 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) # 12
print(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13