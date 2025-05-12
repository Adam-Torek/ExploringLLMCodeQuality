"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""


def sum_negativenum(nums):
    """
    :param nums: list of numbers
    :return: sum of the negative numbers
    """
    return sum(num for num in nums if num < 0)


if __name__ == '__main__':
    print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, -5, -17]))
    print(sum_negativenum([2, 4, 6, 9, 11, 12, 14, 5, 17]))
    print(sum_negativenum([-2, -4, 6, 9, 11, 12, 14, 5, 17]))
    print(sum_negativenum([-2, -4, -6, 9, 11, 12, 14, 5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, 11, 12, 14, 5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, -11, 12, 14, 5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, 14, 5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, 5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, -5, 17]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, -5, -17]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, -5, -17, -19]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, -5, -17, -19, -21]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, -5, -17, -19, -21, -23]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, -5, -17, -19, -21, -23, -25]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, -5, -17, -19, -21, -23, -25, -27]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, -5, -17, -19, -21, -23, -25, -27, -29]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, -5, -17, -19, -21, -23, -25, -27, -29, -31]))
    print(sum_negativenum([-2, -4, -6, -9, -11, -12, -14, -5, -17,