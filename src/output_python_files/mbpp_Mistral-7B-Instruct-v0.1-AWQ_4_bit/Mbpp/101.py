"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""
def kth_element(arr, k):
    """
    Find the kth element in the given array using 1-based indexing.
    """
    if k < 1 or len(arr) < k:
        return None
    return arr[k-1]

# Test the function
arr = [12,3,5,7,19]
k = 2
assert kth_element(arr, k) == 3