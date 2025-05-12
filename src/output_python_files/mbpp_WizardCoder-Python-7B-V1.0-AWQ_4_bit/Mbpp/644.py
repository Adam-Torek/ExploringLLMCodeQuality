"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""

def reverse_Array_Upto_K(arr, k):
    """
    Reverse an array upto a given position
    """
    if k >= len(arr):
        return arr
    else:
        return arr[:k][::-1] + arr[k:]

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4)) # [4, 3, 2, 1, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],2)) # [2, 1, 3, 4, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],0)) # [1, 2, 3, 4, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],5)) # [1, 2, 3, 4, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],1)) # [1, 2, 3, 4, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],3)) # [3, 2, 1, 4, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],6)) # [1, 2, 3, 4, 5, 6]

# Test cases
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],2) == [2, 1, 3, 4, 5, 6]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],0) == [1, 2, 3, 4, 5, 6]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],5) == [1, 2, 3, 4, 5, 6]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],1) == [1, 2, 3, 4, 5, 6]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],3) == [3, 2, 1, 4, 5, 6]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],6) == [1, 2, 3, 4, 5, 6]

# Edge cases
assert reverse_Array_Upto_K([],0) == []
assert reverse_Array_Upto_K([1],0) == [1]
assert reverse_Array_Upto_K([1,2],1) == [2, 1]
assert reverse_Array_Upto_K([1,2],0) == [1, 2]
assert reverse_Array_Upto_K([1,2,3],2) == [2, 1, 3]
assert reverse_Array_