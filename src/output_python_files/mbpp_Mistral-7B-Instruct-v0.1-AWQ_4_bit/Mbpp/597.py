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
    if len(arr1) == 0 or len(arr2) == 0:
        return None
    if k == 0:
        return arr1[0]
    if k == len(arr1) + len(arr2):
        return None
    if k < len(arr1) + len(arr2):
        return find_kth(arr1, arr2, k)
    else:
        return find_kth(arr2, arr1, k - len(arr1) - 1)


# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 6) == 7
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 7) == 9
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 8) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 9) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 10) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 11) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 12) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 13) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 14) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 15) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 16) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 17) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 18) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 19) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 20) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 21) == 10
# assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 22) == 10
# assert find_kth([2, 3, 6