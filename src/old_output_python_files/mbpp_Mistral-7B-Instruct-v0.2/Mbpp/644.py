"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""
def reverse_Array_Upto_K(arr, k):
    start = 0
    end = k
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr[:k+1]

# Test case
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4) == [4, 3, 2, 1, 5, 6]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 2) == [3, 2, 1, 4, 5, 6]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 0) == [1, 2, 3, 4, 5, 6]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 5) == [6, 5, 4, 3, 2, 1]