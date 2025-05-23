"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""

def is_Monotonic(arr):
    if len(arr) <= 1:
        return True
    if arr[0] > arr[1]:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True
    if arr[0] < arr[1]:
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                return False
        return True
    return True

print(is_Monotonic([6, 5, 4, 4]))
print(is_Monotonic([1, 1, 1, 3]))
print(is_Monotonic([1, 3, 2]))
print(is_Monotonic([1, 2, 4, 5]))
print(is_Monotonic([1, 1, 1, 1]))
print(is_Monotonic([1, 1, 3, 3]))
print(is_Monotonic([1, 3, 3, 3]))
print(is_Monotonic([1, 3, 2, 3]))
print(is_Monotonic([1, 2, 2, 3]))
print(is_Monotonic([1, 1, 1, 2]))
print(is_Monotonic([1, 2, 2, 2]))
print(is_Monotonic([1, 2, 3, 3]))
print(is_Monotonic([1, 2, 3, 2]))
print(is_Monotonic([1, 2, 3, 1]))
print(is_Monotonic([1, 2, 1, 2]))
print(is_Monotonic([1, 2, 1, 1]))
print(is_Monotonic([1, 2, 2, 2]))
print(is_Monotonic([1, 2, 2, 1]))
print(is_Monotonic([1, 2, 1, 1]))
print(is_Monotonic([1, 2, 1, 2]))
print(is_Monotonic([1, 1, 2, 2]))
print(is_Monotonic([1, 1, 2, 1]))
print(is_Monotonic([1, 1, 1, 2]))
print(is_Monotonic([1, 1, 1, 1]))
print(is_Monotonic([1, 1, 1, 3]))
print(is_Monotonic([1, 3, 3, 3]))
print(is_Monotonic([1, 3, 3, 2]))
print(is_Monotonic([1, 3, 2, 3]))
print(is_Monotonic([1, 3, 2, 2]))
print(is_Monotonic([1, 3, 2, 1]))
print(is_Monotonic([1, 3, 1, 2]))
print(is_Monotonic([1, 3, 1, 1]))
print(is_Monotonic([1, 3, 3, 3]))
print(is_Monotonic([1, 3, 3, 2]))
print(is_Monotonic([1, 3, 2, 3]))
print(is_Monotonic([1, 3, 2, 2]))
print(is_Monotonic([1, 3, 2, 1]))
print(is_Monotonic([1, 3, 1, 2]))
print(is_Monotonic([1, 3, 1, 1]))
print(is_Monotonic([1, 3, 3, 3]))
print(is_Monotonic([1, 3, 3, 2]))
print(is_Monotonic([1, 3, 2, 3]))
print(is_Monotonic([1, 3, 2, 2]))
print(is_Monotonic([1, 3, 2, 1]))
print(is_Monotonic([1, 3, 1, 2]))
print(is_Monotonic([1, 3, 1, 1]))
print