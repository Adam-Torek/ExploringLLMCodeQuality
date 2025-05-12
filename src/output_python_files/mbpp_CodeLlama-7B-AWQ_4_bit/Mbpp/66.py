"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""


def pos_count(nums):
    """
    :param nums: list of numbers
    :return: number of positive numbers in the list
    """
    count = 0
    for num in nums:
        if num > 0:
            count += 1
    return count


if __name__ == '__main__':
    print(pos_count([1, -2, 3, -4]))
    print(pos_count([1, 2, 3, 4]))
    print(pos_count([-1, -2, -3, -4]))
    print(pos_count([-1, 2, 3, 4]))
    print(pos_count([-1, -2, -3, -4, -5]))
    print(pos_count([-1, -2, -3, -4, -5, -6]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8, -9]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19]))
    print(pos_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]))
    print(pos_count([-1, -2, -3, -4, -5,