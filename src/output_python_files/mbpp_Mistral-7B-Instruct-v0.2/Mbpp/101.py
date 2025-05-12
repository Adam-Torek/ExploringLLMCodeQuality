"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""
def kth_element(arr, k):
    """
    :param arr: list of integers
    :param k: integer representing the index
    :return: the kth element in the list
    """
    arr.sort()
    return arr[k-1]

if __name__ == "__main__":
    arr = [12,3,5,7,19]
    k = 2
    assert kth_element(arr, k) == 3
    print("Test passed!")