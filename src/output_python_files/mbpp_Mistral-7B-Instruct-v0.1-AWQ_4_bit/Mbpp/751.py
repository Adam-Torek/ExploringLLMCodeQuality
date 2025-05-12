"""
Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""

def check_min_heap(arr):
    """
    :param arr: array
    :return: True if arr is min heap, False otherwise
    """
    n = len(arr)
    if n == 0:
        return True
    for i in range(n//2):
        if arr[i] > arr[i+1]:
            return False
    return True