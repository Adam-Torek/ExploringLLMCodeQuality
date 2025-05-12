"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""

def intersection_array(arr1, arr2):
    return list(set(arr1) & set(arr2))

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])) # Output: [1, 2, 8, 9]