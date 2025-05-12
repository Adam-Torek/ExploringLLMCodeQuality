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

    if k <= len(arr1):
        return arr1[k - 1]

    if k <= len(arr1) + len(arr2):
        return arr2[k - len(arr1) - 1]


if __name__ == '__main__':
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 10))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 1))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 0))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 11))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 12))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 13))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 14))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 15))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 16))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 17))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 18))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 19))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 20))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 21))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 22))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 23))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 24))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 25))
    print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 26))
    print