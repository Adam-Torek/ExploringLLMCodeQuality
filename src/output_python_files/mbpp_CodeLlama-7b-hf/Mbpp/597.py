"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""


def find_kth(arr1, arr2, k):
    """
    :param arr1: sorted array
    :param arr2: sorted array
    :param k: kth element
    :return: kth element
    """
    if not arr1 or not arr2:
        return None
    if k > len(arr1) + len(arr2):
        return None
    if k > len(arr1):
        return arr2[k - len(arr1) - 1]
    if k > len(arr2):
        return arr1[k - len(arr2) - 1]
    if k == len(arr1):
        return arr2[k - 1]
    if k == len(arr2):
        return arr1[k - 1]
    if k == 1:
        return min(arr1[0], arr2[0])
    if k == 2:
        return max(arr1[0], arr2[0])
    if k == len(arr1) + len(arr2) - 1:
        return max(arr1[-1], arr2[-1])
    if k == len(arr1) + len(arr2) - 2:
        return min(arr1[-1], arr2[-1])
    if k > len(arr1) // 2:
        return find_kth(arr1, arr2[k - len(arr1) - 1:], k - len(arr1))
    if k > len(arr2) // 2:
        return find_kth(arr1[k - len(arr2) - 1:], arr2, k - len(arr2))
    if k == len(arr1) // 2:
        return max(arr1[k - 1], arr2[k - 1])
    if k == len(arr2) // 2:
        return max(arr1[k - 1], arr2[k - 1])
    if k == len(arr1) // 2 + 1:
        return min(arr1[k - 1], arr2[k - 1])
    if k == len(arr2) // 2 + 1:
        return min(arr1[k - 1], arr2[k - 1])
    if k == len(arr1) // 2 + 2:
        return max(arr1[k - 1], arr2[k - 1])
    if k == len(arr2) // 2 + 2:
        return max(arr1[k - 1], arr2[k - 1])
    if k == len(arr1) // 2 + 3:
        return min(arr1[k - 1], arr2[k - 1])
    if k == len(arr2) // 2 + 3:
        return min(arr1[k - 1], arr2[k - 1])
    if k == len(arr1) // 2 + 4:
        return max(arr1[k - 1], arr2[k - 1])
    if k == len(arr2) // 2 + 4:
        return max(arr1[k - 1], arr2[k - 1])
    if k == len(arr1) // 2 + 5:
        return min(arr1[k - 1], arr2[k - 1])
    if k == len(arr2) // 2 + 5:
        return min(arr1[k - 1], arr2[k - 1])
    if k == len(arr1) // 2 + 6:
        return max(arr1[k - 1], arr2[k - 1])
    if k == len(arr2) // 2 + 6:
        return max(arr1[k - 1], arr2[k - 1])
    if k == len(arr1) // 2 + 7:
        return min(arr1[k - 1], arr2[k - 1])