"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""


def big_diff(lst):
    """
    :param lst: list of integers
    :return: difference between largest and smallest value in a given list
    """
    return max(lst) - min(lst)


if __name__ == '__main__':
    print(big_diff([1, 2, 3, 4]))
    print(big_diff([10, 3, 5, 6]))
    print(big_diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]))
    print(big_diff([10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,