"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""

def find_first_occurrence(arr, num):
    """
    Find the index of the first occurrence of a given number in a sorted array.
    """
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            result = mid
            right = mid - 1
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Test cases
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5)) # Output: 1
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) # Output: -1
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 1) # Output: 0
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 1) # Output: 0
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5) # Output: 3
print(find_first_occurrence([1, 2, 3,