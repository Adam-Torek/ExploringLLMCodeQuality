"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""

def find_first_occurrence(arr, num):
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
print(find_first_occurrence([1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 8], 4) # Output: 2
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 0) # Output: -1
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) # Output: 0
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) # Output: 6
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) # Output: 2
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 8) # Output: 6
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) # Output: 0
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) # Output: 1
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) # Output: 6
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) # Output: -1
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 0) # Output: -1
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) # Output: 0
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) # Output: 2
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 8) # Output: 6
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) # Output: -1
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 0) # Output: -1
print(find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) # Output: 0
print(find_first_occurrence([1, 2, 3, 4, 5, 6,