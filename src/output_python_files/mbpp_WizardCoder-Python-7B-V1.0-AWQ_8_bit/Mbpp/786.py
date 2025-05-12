"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""
def right_insertion(arr, val):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return right

# Test cases
print(right_insertion([1,2,4,5], 6)) # Output: 4
print(right_insertion([1,2,4,5], 3)) # Output: 2
print(right_insertion([1,2,4,5], 0)) # Output: 0
print(right_insertion([1,2,4,5], 10)) # Output: 4
print(right_insertion([1,2,4,5], 1)) # Output: 0
print(right_insertion([1,2,4,5], 5)) # Output: 3
print(right_insertion([1,2,4,5], 4)) # Output: 2
print(right_insertion([1,2,4,5], 2)) # Output: 1
print(right_insertion([1,2,4,5], 10)) # Output: 4
print(right_insertion([1,2,4,5], 0)) # Output: 0
print(right_insertion([1,2,4,5], 1)) # Output: 0
print(right_insertion([1,2,4,5], 5)) # Output: 3
print(right_insertion([1,2,4,5], 4)) # Output: 2
print(right_insertion([1,2,4,5], 2)) # Output: 1
print(right_insertion([1,2,4,5], 10)) # Output: 4