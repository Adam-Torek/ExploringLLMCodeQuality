"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""


def sum_negativenum(nums):
    """
    :param nums: list of numbers
    :return: sum of negative numbers
    """
    return sum(x for x in nums if x < 0)


if __name__ == '__main__':
    print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, -5, -17]))
    print(sum_negativenum([2, 4, 6, 9, 11, 12, 14, 5, 17]))
    print(sum_negativenum([-2, -4, 6, 9, 11, 12, 14, 5, 17]))
    print(sum_negativenum([2, 4, -6, -9, 11, 12, 14, 5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, 11, 12, 14, 5, 17]))
    print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([