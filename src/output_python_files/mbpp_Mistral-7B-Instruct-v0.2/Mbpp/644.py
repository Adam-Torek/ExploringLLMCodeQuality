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
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 3) == [3, 2, 1, 5, 6, 4]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 2) == [2, 1, 5, 6, 4, 3]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 1) == [1, 5, 6, 4, 3, 2]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 0) == [1, 6, 5, 4, 3, 2]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -1) == [1, 2, 3, 4, 5, 6]
assert reverse_Array_Upto_K([], 0) == []
assert reverse_Array_Upto_K([], 1) == []
assert reverse_Array_Upto_K([], 2) == []
assert reverse_Array_Upto_K([], 3) == []
assert reverse_Array_Upto_K([], 4) == []
assert reverse_Array_Upto_K([], 5) == []
assert reverse_Array_Upto_K([], 6) == []
assert reverse_Array_Upto_K([], 7) == []
assert reverse_Array_Upto_K([], 8) == []
assert reverse_Array_Upto_K([], 9) == []
assert reverse_Array_Upto_K([], 10) == []
assert reverse_Array_Upto_K([], 11) == []
assert reverse_Array_Upto_K([], 12) == []
assert reverse_Array_Upto_K([], 13) == []
assert reverse_Array_Upto_K([], 14) == []
assert reverse_Array_Upto_K([], 15) == []
assert reverse_Array_Upto_K([], 16) == []
assert reverse_Array_Upto_K([], 17) == []
assert reverse_Array_Upto_K([], 18) == []
assert reverse_Array_Upto_K([], 19) == []
assert reverse_Array_Upto_K([], 20) == []
assert reverse_Array_Upto_K([], 21) == []
assert reverse_Array_Upto_K([], 22) == []
assert reverse_Array_Upto_K([], 23) == []
assert reverse_Array_Upto_K([], 24) == []
assert reverse_Array_Upto_K([], 25) == []
assert reverse_Array_Upto_K([], 26) == []
assert reverse_Array_Upto_K([], 27) == []
assert reverse_Array_Upto_K([], 28) == []