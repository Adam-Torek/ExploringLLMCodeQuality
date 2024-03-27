"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""

def max_subarray_product(arr):
    max_product = 0
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= arr[j]
            if product > max_product:
                max_product = product
    return max_product

print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))
<file_sep>/01_Data_Structures/01_Arrays/01_Array_Rotation.py
"""
Write a function that rotates an array to the right by k steps.

For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [5, 6, 1, 2, 3, 4].

You can assume that 0 <= k <= length of the array.
"""

def rotate_array(arr, k):
    if k == 0:
        return arr
    else:
        return arr[k:] + arr[:k]

print(rotate_array([1, 2, 3, 4, 5, 6], 2))
<file_sep>/01_Data_Structures/01_Arrays/02_Array_Rotation_2.py
"""
Write a function that rotates an array to the right by k steps.

For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [5, 6, 1, 2, 3, 4].

You can assume that 0 <= k <= length of the array.
"""

def rotate_array(arr, k):
    if k == 0:
        return arr
    else:
        return arr[-k:] + arr[:-k]

print(rotate_array([1, 2, 3, 4, 5, 6], 2))
<file_sep>/01_Data_Structures/01_Arrays/03_Array_Rotation_3.py
"""
Write a function that rotates an array to the right by k steps.

For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [5, 6, 1, 2, 3, 4].

You can assume that 0 <= k <= length of the array.
"""

def rotate_array(arr, k):
    if k == 0:
        return arr
    else:
        return arr[len(arr) - k:] + arr[:len(arr) - k]

print(rotate_array([1, 2, 3, 4, 5, 6], 2))
<file_sep>/01_Data_Structures/01_Arrays/04_Array_Rotation_4.py
"""
Write a function that rotates an array to the right by k steps.

For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [5, 6, 1, 2, 3, 4].

You can assume that 0 <= k <= length of the array.
"""

def rotate_array(arr, k):
    if k == 0:
        return arr
    else:
        return arr[len(arr) - k:] + arr[:len(arr) - k]

def rotate_array_2(arr, k):
    if k == 0:
        return arr
    else:
        return arr[-k:] + arr[:-k]

print(rotate_array([1, 2, 3, 4, 5, 6], 2))
print(rotate_array_2([1, 2, 3, 4, 5, 6], 2))
<file_sep>/01_Data_Structures/01_Arrays/05_Array_Rotation_5.py
"""
Write a function that rotates an array to the right by k steps.

For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [5, 6, 1, 2, 3, 4].

You can assume that 0 <= k <= length of the array.
"""