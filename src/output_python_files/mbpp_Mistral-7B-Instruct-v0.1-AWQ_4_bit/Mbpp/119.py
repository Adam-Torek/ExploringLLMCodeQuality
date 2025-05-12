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
        count = 1
        while i < n-1 and arr[i] == arr[i+1]:
            count += 1
            i += 1
        if count == 1:
            return arr[i]
    return None