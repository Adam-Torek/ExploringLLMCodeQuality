"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""


def second_smallest(nums):
    """
    :param nums: list of numbers
    :return: second smallest number in the list
    """
    if len(nums) < 2:
        return None
    if len(nums) == 2:
        return nums[1]
    nums.sort()
    return nums[1]


if __name__ == '__main__':
    print(second_smallest([1, 2, -8, -2, 0, -2]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4, 5]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4, 5, 6]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4, 5, 6, 7]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4, 5, 6, 7, 8]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,