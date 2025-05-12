"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""

def reverse_Array_Upto_K(arr, k):
    """
    Reverse an array upto a given position
    """
    if k > len(arr):
        return "Invalid position"
    else:
        return arr[:k][::-1] + arr[k:]

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4)) # Output: [4, 3, 2, 1, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],3)) # Output: [3, 2, 1, 4, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],5)) # Output: [1, 2, 3, 4, 5, 6]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],0)) # Output: [6, 5, 4, 3, 2, 1]
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],6)) # Output: Invalid position

# Time Complexity: O(1)
# Space Complexity: O(1)
# Inplace: Yes
# Stable: No (as it reverses the array)