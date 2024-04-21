"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""

def is_Monotonic(arr):
    if len(arr) < 2:
        return True
    if arr[0] <= arr[1]:
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True
    else:
        for i in range(1, len(arr)):
            if arr[i] >= arr[i-1]:
                return False
        return True

# Test cases
print(is_Monotonic([6, 5, 4, 4])) # True
print(is_Monotonic([1, 2, 3, 4])) # True
print(is_Monotonic([1, 2, 3, 4, 5])) # False
print(is_Monotonic([1, 2, 3, 4, 5, 6])) # False<|endoftext|>