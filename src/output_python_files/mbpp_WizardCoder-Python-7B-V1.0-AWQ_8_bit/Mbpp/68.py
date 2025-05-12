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
print(is_monotonic([6, 5, 4, 5])) # False
print(is_monotonic([1, 2, 3, 2, 1])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9])) # True
print(is_monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # True
print(is_monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 7, 6, 5, 4, 3, 2, 1])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # True
print(is_monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # True
print(is_monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # False
print(is_monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])) # True
print(is_monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 16, 15, 14, 13, 12, 1