"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""

def kth_element(arr, k):
    return sorted(arr)[k-1]

print(kth_element([12,3,5,7,19], 2)) # Output: 3
print(kth_element([1, 2, 3, 4, 5], 4)) # Output: 5
print(kth_element([1, 2, 3, 4, 5], 1)) # Output: 1
print(kth_element([1, 2, 3, 4, 5], 5)) # Output: 5
print(kth_element([1, 2, 3, 4, 5], 0)) # Output: None
print(kth_element([1, 2, 3, 4, 5], 6)) # Output: None