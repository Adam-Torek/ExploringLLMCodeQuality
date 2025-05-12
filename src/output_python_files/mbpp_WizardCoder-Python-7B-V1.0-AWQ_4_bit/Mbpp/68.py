"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""

def is_monotonic(arr):
    if arr == sorted(arr):
        return True
    elif arr == sorted(arr, reverse=True):
        return True
    else:
        return False

# Test cases
print(is_monotonic([6, 5, 4, 4])) # True
print(is_monotonic([1, 2, 2, 3, 4, 5])) # True
print(is_monotonic([1, 2, 3, 4, 5])) # True
print(is_monotonic([6, 5, 3, 4])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6])) # False
print(is_monotonic([1, 2, 2, 1])) # False
print(is_monotonic([1, 1, 1])) # True
print(is_monotonic([6, 5, 4, 3, 4])) # False
print(is_monotonic([1, 2, 3, 2, 1])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6])) # False
print(is_monotonic([1, 2, 3, 4, 4, 5])) # False
print(is_monotonic([1, 2, 3, 4, 4, 5])) # False
print(is_monotonic([1, 2, 2, 3, 4, 5])) # False
print(is_monotonic([1, 2, 3, 4, 4, 5])) # False
print(is_monotonic([1, 2, 3, 4, 5, 5])) # False
print(is_monotonic([1, 2, 3, 4, 4, 5])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6])) # False
print(is_monotonic([1, 2, 3, 4, 5, 5])) # False
print(is_monotonic([1, 2, 3, 4, 4, 5])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6])) # False
print(is_monotonic([1, 2, 3, 4, 4, 5])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6])) # False
print(is_monotonic([1, 2, 3, 4, 5, 5])) # False
print(is_monotonic([1, 2, 3, 4, 4, 5])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6])) # False
print(is_monotonic([1, 2, 3, 4, 4, 5])) # False
print(is_monotonic([1, 2, 3, 4, 5, 5])) # False
print(is_monotonic([1, 2, 3, 4, 4, 5])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6])) # False
print(is_monotonic([1, 2, 3, 4, 5, 5])) # False
print(is_monotonic([1, 2, 3, 4, 4, 5])) # False
print(is_monotonic([