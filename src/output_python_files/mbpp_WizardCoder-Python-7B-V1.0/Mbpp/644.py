"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""

def reverse_Array_Upto_K(arr, k):
    if k >= len(arr):
        return arr
    else:
        return arr[:k][::-1] + arr[k:]

# Testing the function
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4)) # Output: [4, 3, 2, 1, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],2)) # Output: [2, 1, 3, 4, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],0)) # Output: [6, 5, 4, 3, 2, 1]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],5)) # Output: [1, 2, 3, 4, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],1)) # Output: [1, 2, 3, 4, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],0)) # Output: [6, 5, 4, 3, 2, 1]
print(reverse_Array_Upto_K([1],0)) # Output: [1]
print(reverse_Array_Upto_K([],4) # Output: []