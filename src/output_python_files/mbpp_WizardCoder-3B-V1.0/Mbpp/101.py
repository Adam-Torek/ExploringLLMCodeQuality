"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""

def kth_element(arr, k):
    return arr[k-1]

# Test the function
print(kth_element([12,3,5,7,19], 2)) # Output: 3<|endoftext|>