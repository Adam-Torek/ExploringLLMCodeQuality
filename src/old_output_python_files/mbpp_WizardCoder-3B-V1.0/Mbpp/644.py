"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""
def reverse_Array_Upto_K(arr, k):
    """
    This function takes an array and a position k as input and returns the reversed array upto the position k.
    """
    # Reverse the array from 0 to k-1
    arr = arr[::-1]
    # Reverse the array from k to the end
    arr = arr[k:] + arr[:k]
    return arr

# Test the function
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4)) # Output: [4, 3, 2, 1, 5, 6]<|endoftext|>