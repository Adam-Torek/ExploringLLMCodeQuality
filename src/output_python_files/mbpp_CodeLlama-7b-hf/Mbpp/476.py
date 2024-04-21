"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""


def big_sum(arr):
    """
    :param arr: list of integers
    :return: sum of the largest and smallest value in a given array
    """
    return max(arr) + min(arr)


if __name__ == '__main__':
    print(big_sum([1, 2, 3]))
    print(big_sum([1, 2, 3, 4]))
    print(big_sum([1, 2, 3, 4, 5]))
    print(big_sum([1, 2, 3, 4, 5, 6]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(big_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))
    print(big_sum([1, 2, 3, 4, 5,