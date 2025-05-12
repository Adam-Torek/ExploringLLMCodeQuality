"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""

def search(arr):
    """
    :param arr: sorted array
    :return: element that appears only once
    """
    n = len(arr)
    for i in range(n):
        if arr[i] == arr[i+1]:
            return None
    return arr[0]


# test
arr = [1, 1, 2, 2, 3]
assert search(arr) == 3