"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""

def is_Sub_Array(arr1, arr2):
    if len(arr1) > len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            return True
    return False

# Test cases
print(is_Sub_Array([1,4,3,5],[1,2])) # False
print(is_Sub_Array([1,4,3,5],[1,4,3,5])) # True
print(is_Sub_Array([1,4,3,5],[1,4,3])) # True<|endoftext|>