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
/02_data_structures/01_arrays/02_reverse_array.py
"""
Write a function to reverse an array.
assert reverse([1, 2, 3, 4]) == [4, 3, 2, 1]
"""

def reverse(arr):
    return arr[::-1]

print(reverse([1, 2, 3, 4]))
/02_data_structures/01_arrays/03_rotate_array.py
"""
Write a function to rotate an array to the right by k steps.
assert rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
"""

def rotate(arr, k):
    return arr[-k:] + arr[:-k]

print(rotate([1, 2, 3, 4, 5], 2))
/02_data_structures/01_arrays/04_find_missing_number.py
"""
Write a function to find the missing number in a given integer array of 1 to 100.
assert find_missing_number([1, 2, 3, 4, 6, 7, 8, 10]) == 5
"""

def find_missing_number(arr):
    for i in range(1, 101):
        if i not in arr:
            return i

print(find_missing_number([1, 2, 3, 4, 6, 7, 8, 10]))
/02_data_structures/01_arrays/05_find_duplicate.py
"""
Write a function to find the first duplicate value in the given array.
assert find_duplicate([1, 2, 3, 1]) == 1
"""

def find_duplicate(arr):
    for i in range(len(arr)):
        if arr[i] in arr[i+1:]:
            return arr[i]

print(find_duplicate([1, 2, 3, 1]))
/02_data_structures/01_arrays/06_find_common_elements.py
"""
Write a function to find common elements between two arrays.
assert find_common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
"""

def find_common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))

print(find_common_elements([1, 2, 3], [2, 3, 4]))
/02_data_structures/01_arrays/07_find_unique_elements.py
"""
Write a function to find unique elements in an array.
assert find_unique_elements([1, 2, 3, 1]) == [2, 3]
"""

def find_unique_elements(arr):
    return list(set(arr) - set(arr[::2]))

print(find_unique_elements([1, 2, 3, 1]))
/02_data_structures/01_arrays/08_find_missing_elements.py
"""
Write a function to find missing elements in an array.
assert find_missing_elements([1