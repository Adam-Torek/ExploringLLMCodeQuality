"""
Write a function to compute the n-th power of each number in a list.
assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""


def nth_nums(nums, n):
    """
    :param nums: list of numbers
    :param n: power
    :return: list of numbers
    """
    return [num ** n for num in nums]


if __name__ == '__main__':
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 13))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 16))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 17))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 18))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20))
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2