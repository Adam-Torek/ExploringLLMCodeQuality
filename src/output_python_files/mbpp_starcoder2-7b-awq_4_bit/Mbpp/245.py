"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""

def max_sum(arr):
    """
    :param arr: list
    :return: int
    """
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)
    max_sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if i == 0 and j == len(arr) - 1:
                continue
            if i == 0:
                max_sum = max(max_sum, sum(arr[i:j + 1]))
            elif j == len(arr) - 1:
                max_sum = max(max_sum, sum(arr[i:j + 1]))
            else:
                max_sum = max(max_sum, sum(arr[i:j + 1]))
    return max_sum


def max_sum_2(arr):
    """
    :param arr: list
    :return: int
    """
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)
    max_sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if i == 0 and j == len(arr) - 1:
                continue
            if i == 0:
                max_sum = max(max_sum, sum(arr[i:j + 1]))
            elif j == len(arr) - 1:
                max_sum = max(max_sum, sum(arr[i:j + 1]))
            else:
                max_sum = max(max_sum, sum(arr[i:j + 1]))
    return max_sum


def max_sum_3(arr):
    """
    :param arr: list
    :return: int
    """
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)
    max_sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if i == 0 and j == len(arr) - 1:
                continue
            if i == 0:
                max_sum = max(max_sum, sum(arr[i:j + 1]))
            elif j == len(arr) - 1:
                max_sum = max(max_sum, sum(arr[i:j + 1]))
            else:
                max_sum = max(max_sum, sum(arr[i:j + 1]))
    return max_sum


def max_sum_4(arr):
    """
    :param arr: list
    :return: int
    """
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)
    max_sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if i == 0 and j == len(arr) - 1:
                continue
            if i == 0:
                max_sum = max(max_sum, sum(arr[i:j + 1]))
            elif j == len(arr) - 1:
                max_sum = max(max_sum, sum(arr[i:j + 1]))
            else:
                max_sum = max(max_sum, sum(arr[i:j + 1]))
    return max_sum


def max_sum_5(arr):
    """
    :param arr: list
    :return: int
    """
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)
    max_sum = 0
    for i