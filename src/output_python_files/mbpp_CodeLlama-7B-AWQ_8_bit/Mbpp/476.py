"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""


def big_sum(array):
    """
    :param array: array of integers
    :return: sum of the largest and smallest value in the array
    """
    return max(array) + min(array)


if __name__ == '__main__':
    print(big_sum([1, 2, 3]))
    print(big_sum([10, 5, 20]))
    print(big_sum([10, 5, 20, 3, 1]))
    print(big_sum([10, 5, 20, 3, 1, 100]))
    print(big_sum([10, 5, 20, 3, 1, 100, 1000]))
    print(big_sum([10, 5, 20, 3, 1, 100, 1000, 10000]))
    print(big_sum([10, 5, 20, 3, 1, 100, 1000, 10000, 100000]))
    print(big_sum([10, 5, 20, 3, 1, 100, 1000, 10000, 100000, 1000000]))
    print(big_sum([10, 5, 20, 3, 1, 100, 1000, 10000, 100000, 1000000, 10000000]))
    print(big_sum([10, 5, 20, 3, 1, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]))
    print(big_sum([10, 5, 20, 3, 1, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]))
    print(big_sum([10, 5, 20, 3, 1, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]))
    print(big_sum([10, 5, 20, 3, 1, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000]))
    print(big_sum([10, 5, 20, 3, 1, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000]))
    print(big_sum([10, 5, 20, 3, 1, 100, 1000, 10000, 1000