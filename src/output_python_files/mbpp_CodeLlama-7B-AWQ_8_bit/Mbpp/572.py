"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""


def two_unique_nums(nums):
    """
    :param nums: list of numbers
    :return: list of unique numbers
    """
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums


if __name__ == '__main__':
    print(two_unique_nums([1, 2, 3, 2, 3, 4, 5]))
    print(two_unique_nums([1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5]))
    print(two_unique_nums([1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5]))
    print(two_unique_nums([1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5]))
    print(two_unique_nums([1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5]))
    print(two_unique_nums([1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5]))
    print(two_unique_nums([1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5, 1, 2