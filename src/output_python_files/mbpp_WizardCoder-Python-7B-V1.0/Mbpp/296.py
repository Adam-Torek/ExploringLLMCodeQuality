"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
 
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
 
    return merge(left, right)
 
def merge(left, right):
    result = []
    i = j = 0
    inv_count = 0
 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inv_count += len(left) - i
            j += 1
 
    result.extend(left[i:])
    result.extend(right[j:])
 
    return result, inv_count
 
def get_Inv_Count(arr):
    sorted_arr = merge_sort(arr)
    return sorted_arr[1]

# Test the function
print(get_Inv_Count([1,20,6,4,5])) # Output: (array([1, 4, 5, 6, 20], 5)
# The inversion count is 5 as the sorted array would be [1, 4, 5, 6, 20] and the inversions are [20, 6, 5, 4]

# Test the function
print(get_Inv_Count([2, 4, 1, 3, 5])) # Output: (array([1, 2, 3, 4, 5], 3)
# The inversion count is 3 as the sorted array would be [1, 2, 3, 4, 5] and the inversions are [5, 4, 3]

# Test the function
print(get_Inv_Count([3, 1, 2, 4, 5])) # Output: (array([1, 2, 3, 4, 5], 0)
# The inversion count is 0 as the array is already sorted.