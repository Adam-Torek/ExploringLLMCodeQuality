"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""

def reverse_Array_Upto_K(arr,k):
    arr[0:k+1] = arr[k::-1]
    return arr

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))
/Python/Array/Array_Rotation.py
"""
Write a python function to rotate an array by k positions.
assert rotate_Array([1, 2, 3, 4, 5, 6], 4) == [5, 6, 1, 2, 3, 4]
"""

def rotate_Array(arr,k):
    return arr[k:] + arr[:k]

print(rotate_Array([1, 2, 3, 4, 5, 6], 4))
/Python/Array/Array_Rotation_2.py
"""
Write a python function to rotate an array by k positions.
assert rotate_Array_2([1, 2, 3, 4, 5, 6], 4) == [3, 4, 5, 6, 1, 2]
"""

def rotate_Array_2(arr,k):
    return arr[k:] + arr[:k]

print(rotate_Array_2([1, 2, 3, 4, 5, 6], 4))
/Python/Array/Array_Rotation_3.py
"""
Write a python function to rotate an array by k positions.
assert rotate_Array_3([1, 2, 3, 4, 5, 6], 4) == [2, 3, 4, 5, 6, 1]
"""

def rotate_Array_3(arr,k):
    return arr[k:] + arr[:k]

print(rotate_Array_3([1, 2, 3, 4, 5, 6], 4))
/Python/Array/Array_Rotation_4.py
"""
Write a python function to rotate an array by k positions.
assert rotate_Array_4([1, 2, 3, 4, 5, 6], 4) == [1, 2, 3, 4, 5, 6]
"""

def rotate_Array_4(arr,k):
    return arr[k:] + arr[:k]

print(rotate_Array_4([1, 2, 3, 4, 5, 6], 4))
/Python/Array/Array_Rotation_5.py
"""
Write a python function to rotate an array by k positions.
assert rotate_Array_5([1, 2, 3, 4, 5, 6], 4) == [6, 1, 2, 3, 4, 5]
"""

def rotate_Array_5(arr,k):
    return arr[k:] + arr[:k]

print(rotate_Array_5([1, 2, 3, 4, 5, 6], 4))
/Python/Array/Array_Rotation_6.py
"""
Write a python function to rotate an array by k positions.
assert rotate_Array_6([1, 2, 3, 4, 5, 6], 4) == [5, 6, 1, 2, 3, 4]
"""

def rotate_Array_6(arr,k):
    return arr[k:] + arr[:k]

print(rotate_Array_6([1, 2, 3, 4, 5, 6], 4))
/Python/Array/Array_Rotation_7.py
"""
Write a python function to rotate an array by k positions.
assert rotate_Array_7([1, 2, 3, 4, 5, 6], 4) == [4, 5, 6, 1, 2, 3]
"""

def rotate_Array_7(arr,k):
    return arr[k:] + arr[:k]

print(