"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""


def max_sub_array_sum(arr, n):
    """
    :param arr: list of integers
    :param n: integer
    :return: integer
    """
    max_sum = 0
    curr_sum = 0
    for i in arr:
        curr_sum += i
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


if __name__ == '__main__':
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 12))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 14))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 16))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 18))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 20))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 22))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 24))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 26))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 28))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 30))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 32))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 34))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 36))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 38))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 40))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 42))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 44))
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 46))
    print(max_sub_array_sum([-2, -3, 4, -1, -2,