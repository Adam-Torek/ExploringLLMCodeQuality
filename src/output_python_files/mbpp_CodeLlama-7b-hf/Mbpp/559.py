"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""


def max_sub_array_sum(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: integer
    """
    max_sum = 0
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if i >= k:
            curr_sum -= arr[i - k]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum


if __name__ == '__main__':
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 3))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 1))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 0))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 100))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 1000))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10000))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 100000))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 1000000))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10000000))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 100000000))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 1000000000))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10000000000))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 100000000000))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 1000000000000))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10000000000000))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 100000000000000))
    print(max_sub_array_sum([