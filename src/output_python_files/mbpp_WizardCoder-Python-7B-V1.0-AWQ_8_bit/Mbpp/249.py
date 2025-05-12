"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""

def intersection_array(arr1, arr2):
    return list(set(arr1) & set(arr2))

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])) #[1, 2, 8, 9]
print(intersection_array([1, 2, 3, 4, 5, 6, 7],[2, 4, 6, 8, 10])) #[2, 4, 6]
print(intersection_array([1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7, 8, 9])) #[1, 2, 3, 4, 5, 6, 7]
print(intersection_array([1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7, 8, 9])) #[1, 2, 3, 4, 5, 6, 7]
print(intersection_array([1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #[1, 2, 3, 4, 5, 6, 7]
print(intersection_array([1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) #[1, 2, 3, 4, 5, 6, 7]
print(intersection_array([1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) #[1, 2, 3, 4, 5, 6, 7]
print(intersection_array([1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) #[1, 2, 3, 4, 5, 6, 7]
print(intersection_array([1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) #[1, 2, 3, 4, 5, 6, 7]
print(intersection_array([1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) #[1, 2, 3, 4, 5, 6, 7]

# Output:
# [1, 2, 8, 9]
# [2, 4, 6]
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7]
# [1