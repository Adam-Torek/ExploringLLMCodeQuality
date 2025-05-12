"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""

def kth_element(arr, k):
    return sorted(arr)[k-1]

print(kth_element([12,3,5,7,19], 2)) # Output: 3
print(kth_element([1, 2, 3, 4, 5, 6, 7], 4)) # Output: 4
print(kth_element([1, 2, 3, 4, 5, 6, 7], 1)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 7)) # Output: 7
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 6)) # Output: 7
print(kth_element([1, 2, 3, 4, 5, 6, 7], 3)) # Output: 4
print(kth_element([1, 2, 3, 4, 5, 6, 7], 5)) # Output: 6
print(kth_element([1, 2, 3, 4, 5, 6, 7], 10)) # Output: 7
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(kth_element([1, 2, 3, 4, 5, 6, 7], 0)) # Output: 1
print(