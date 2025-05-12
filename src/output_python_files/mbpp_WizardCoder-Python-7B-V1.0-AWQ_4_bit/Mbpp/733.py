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

print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5)) # Output: 1
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 6)) # Output: 3
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 1)) # Output: -1
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 9)) # Output: 6
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 8)) # Output: 5
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 10)) # Output: -1

# Time Complexity: O(log n)
# Space Complexity: O(1)