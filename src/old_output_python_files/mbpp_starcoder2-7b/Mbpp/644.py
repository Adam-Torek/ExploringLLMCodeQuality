"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""

def reverse_Array_Upto_K(arr,k):
    for i in range(k):
        arr[i],arr[k-i-1] = arr[k-i-1],arr[i]
    return arr

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))
<file_sep>/Python/Array/Array_Rotation.py
"""
Write a python function to rotate an array by k positions.
assert rotate_Array([1, 2, 3, 4, 5, 6],4) == [5, 6, 1, 2, 3, 4]
"""

def rotate_Array(arr,k):
    for i in range(k):
        arr.insert(0,arr.pop())
    return arr

print(rotate_Array([1, 2, 3, 4, 5, 6],4))
<file_sep>/Python/Array/Array_Rotation_2.py
"""
Write a python function to rotate an array by k positions.
assert rotate_Array([1, 2, 3, 4, 5, 6],4) == [5, 6, 1, 2, 3, 4]
"""

def rotate_Array(arr,k):
    for i in range(k):
        arr.insert(0,arr.pop())
    return arr

def rotate_Array_2(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

print(rotate_Array_2([1, 2, 3, 4, 5, 6],4))
<file_sep>/Python/Array/Array_Rotation_3.py
"""
Write a python function to rotate an array by k positions.
assert rotate_Array([1, 2, 3, 4, 5, 6],4) == [5, 6, 1, 2, 3, 4]
"""

def rotate_Array(arr,k):
    for i in range(k):
        arr.insert(0,arr.pop())
    return arr

def rotate_Array_3(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_4(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_5(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_6(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_7(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_8(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_9(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_10(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_11(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_12(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_13(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_14(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_15(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_16(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_17(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_18(arr,k):
    arr = arr[k:] + arr[:k]
    return arr

def rotate_Array_19