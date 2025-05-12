"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""

def last(arr, x):
    """
    This function takes an array and an element as input and returns the last position of the element in the array.
    """
    if x not in arr:
        return -1
    else:
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == x:
                return i


# Test the function
arr = [1, 2, 3]
assert last(arr, 1) == 0
assert last(arr, 4) == -1