"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""

def last(arr, x):
    """
    This function takes an array and an element as input and returns the index of the last occurrence of the element in the array.
    """
    if x not in arr:
        return -1
    else:
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == x:
                return i
        return -1


# Test the function
arr = [1,2,3]
assert last(arr,1) == 0
assert last(arr,2) == 1
assert last(arr,3) == 2
assert last(arr,4) == -1