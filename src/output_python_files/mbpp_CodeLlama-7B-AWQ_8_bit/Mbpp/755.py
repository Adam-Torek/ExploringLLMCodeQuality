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
    else:
        nums.sort()
        return nums[1]


if __name__ == '__main__':
    print(second_smallest([1, 2, -8, -2, 0, -2]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12, 13]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12, 13, 14]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12, 13, 14, 15]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12, 13, 14, 15, 16]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]))
    print(second_smallest([1, 2, -8, -2, 0, -2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23