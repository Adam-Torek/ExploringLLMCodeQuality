"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""

def is_monotonic(arr):
    if len(arr) == 1:
        return True
    elif len(arr) == 2:
        return True
    elif arr[0] <= arr[1]:
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True
    elif arr[0] >= arr[1]:
        for i in range(1, len(arr)-1):
            if arr[i] < arr[i+1]:
                return False
        return True

# Test cases
print(is_monotonic([6, 5, 4, 4])) # True
print(is_monotonic([1, 2, 3, 4, 5, 6])) # True
print(is_monotonic([6, 5, 3, 4])) # False
print(is_monotonic([1, 2, 3, 4, 5])) # True
print(is_monotonic([6, 5, 4, 3])) # False
print(is_monotonic([1, 2, 3, 2, 1])) # False
print(is_monotonic([1])) # True
print(is_monotonic([1, 1, 1, 1, 1])) # True
print(is_monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # False
print(is_monotonic([1,