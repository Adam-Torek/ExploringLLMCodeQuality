"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""
def last(arr, x):
    """
    This function takes in a sorted array and an element x and returns the index of the last occurrence of x in the array.
    If x is not found in the array, it returns -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left if left!= len(arr) and arr[left] == x else -1

# Test cases
assert last([1,2,3],1) == 0
assert last([1,2,3,3],3) == 2
assert last([1,2,3,3],4) == -1
assert last([1,2,3,3],2) == 1<|endoftext|>