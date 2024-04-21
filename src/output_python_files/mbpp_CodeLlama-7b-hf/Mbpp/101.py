"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""


def kth_element(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: kth element in the array
    """
    if k > len(arr):
        return None
    return _kth_element(arr, k)


def _kth_element(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: kth element in the array
    """
    if len(arr) == 1:
        return arr[0]
    if k == 1:
        return arr[0]
    if k == len(arr):
        return arr[-1]
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    if k == len(left) + 1:
        return pivot
    elif k > len(left) + 1:
        return _kth_element(right, k - len(left) - 1)
    else:
        return _kth_element(left, k)


if __name__ == '__main__':
    print(kth_element([12, 3, 5, 7, 19], 2))
    print(kth_element([12, 3, 5, 7, 19], 3))
    print(kth_element([12, 3, 5, 7, 19], 4))
    print(kth_element([12, 3, 5, 7, 19], 5))
    print(kth_element([12, 3, 5, 7, 19], 6))
    print(kth_element([12, 3, 5, 7, 19], 7))
    print(kth_element([12, 3, 5, 7, 19], 8))
    print(kth_element([12, 3, 5, 7, 19], 9))
    print(kth_element([12, 3, 5, 7, 19], 10))
    print(kth_element([12, 3, 5, 7, 19], 11))
    print(kth_element([12, 3, 5, 7, 19], 12))
    print(kth_element([12, 3, 5, 7, 19], 13))
    print(kth_element([12, 3, 5, 7, 19], 14))
    print(kth_element([12, 3, 5, 7, 19], 15))
    print(kth_element([12, 3, 5, 7, 19], 16))
    print(kth_element([12, 3, 5, 7, 19], 17))
    print(kth_element([12, 3, 5, 7, 19], 18))
    print(kth_element([12, 3, 5, 7, 19], 19))
    print(kth_element([12, 3, 5, 7, 19], 20))
    print(kth_element([12, 3, 5, 7, 19], 21))
    print(kth_element([12, 3, 5, 7, 19], 22))
    print(kth_element([12, 3, 5, 7, 19], 23))
    print(kth_element([12, 3, 5, 7, 19], 24))
    print(kth_element([12, 3, 5, 7,