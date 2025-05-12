"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""
def kth_element(arr, k):
    """
    :param arr: array
    :param k: kth element
    :return: kth element
    """
    if k < 1 or len(arr) < k:
        return None
    else:
        return arr[k - 1]

# test
arr = [12,3,5,7,19]
k = 2
print(kth_element(arr, k))