"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""

def is_Monotonic(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    if len(arr) < 2:
        return True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True