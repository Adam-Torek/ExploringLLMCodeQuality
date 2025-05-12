"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""

def find_kth(arr1, arr2, k):
    """
    :param arr1: first sorted array
    :param arr2: second sorted array
    :param k: kth element
    :return: kth element
    """
    if len(arr1) == 0:
        return arr2[k - 1]
    if len(arr2) == 0:
        return arr1[k - 1]
    if k == 0:
        return arr1[0]
    if k == len(arr1) + len(arr2):
        return arr2[0]
    if k < len(arr1) + len(arr2):
        return find_kth(arr1, arr2[:k], k)
    else:
        return find_kth(arr1[:k], arr2, k)


# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 6) == 9
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 7) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 8) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 9) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 10) == 10