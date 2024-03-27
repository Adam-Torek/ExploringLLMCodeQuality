"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""


def max_sub_array_sum(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: sum of the largest contiguous sublist
    """
    if not arr or k <= 0:
        return 0
    max_sum = 0
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[i - k + 1]
    return max_sum


if __name__ == '__main__':
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 4))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 2))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 1))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 0))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -1))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -2))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -3))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -4))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -5))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -6))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -7))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -8))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -9))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -10))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -11))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -12))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -13))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -14))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -15))
    print(max_sub