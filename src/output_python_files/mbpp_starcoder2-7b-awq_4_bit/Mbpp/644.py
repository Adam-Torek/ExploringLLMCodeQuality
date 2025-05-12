"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""

def reverse_Array_Upto_K(arr,k):
    arr = arr[::-1]
    arr = arr[:k]
    return arr

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))
/Python/Array/Array_Rotation.py
"""
Write a python function to rotate an array by k positions.
assert rotate_Array_By_K([1, 2, 3, 4, 5, 6],4) == [5, 6, 1, 2, 3, 4]
"""

def rotate_Array_By_K(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

print(rotate_Array_By_K([1, 2, 3, 4, 5, 6],4))
/Python/Array/Array_Intersection.py
"""
Write a python function to find the intersection of two arrays.
assert intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3, 4, 5]
"""

def intersection(arr1,arr2):
    return list(set(arr1).intersection(arr2))

print(intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
/Python/Array/Array_Union.py
"""
Write a python function to find the union of two arrays.
assert union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
"""

def union(arr1,arr2):
    return list(set(arr1).union(arr2))

print(union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
/Python/Array/Array_Difference.py
"""
Write a python function to find the difference of two arrays.
assert difference([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [1, 2]
"""

def difference(arr1,arr2):
    return list(set(arr1).difference(arr2))

print(difference([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
/Python/Array/Array_Flatten.py
"""
Write a python function to flatten an array.
assert flatten([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
"""

def flatten(arr):
    return [item for sublist in arr for item in sublist]

print(flatten([[1, 2, 3], [4, 5, 6]]))
/Python/Array/Array_Sum.py
"""
Write a python function to find the sum of all the elements in an array.
assert sum_Array([1, 2, 3, 4, 5]) == 15
"""

def sum_Array(arr):
    return sum(arr)

print(sum_Array([1, 2, 3, 4, 5]))
/Python/Array/Array_Max.py
"""
Write a python function to find the maximum value in an array.
assert max_Array([1, 2, 3, 4, 5]) == 5
"""

def max_Array(arr):
    return max(arr)

print(max_Array([1, 2