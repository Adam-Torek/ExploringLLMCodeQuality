"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""


def smallest_num(nums):
    """
    :param nums: list of numbers
    :return: smallest number in the list
    """
    if not nums:
        return None
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest


if __name__ == '__main__':
    print(smallest_num([10, 20, 1, 45, 99]))
    print(smallest_num([10, 20, 1, 45, 99, 100]))
    print(smallest_num([10, 20, 1, 45, 99, 100, 101]))
    print(smallest_num([10, 20, 1, 45, 99, 100, 101, 102]))
    print(smallest_num([10, 20, 1, 45, 99, 100, 101, 102, 103]))
    print(smallest_num([10, 20, 1, 45, 99, 100, 101, 102, 103, 104]))
    print(smallest_num([10, 20, 1, 45, 99, 100, 101, 102, 103, 104, 105]))
    print(smallest_num([10, 20, 1, 45, 99, 100, 101, 102, 103, 104, 105, 106]))
    print(smallest_num([10, 20, 1, 45, 99, 100, 101, 102, 103, 104, 105, 106, 107]))
    print(smallest_num([10, 20, 1, 45, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]))
    print(smallest_num([10, 20, 1, 45, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]))
    print(smallest_num([10, 20, 1, 45, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]))
    print(smallest_num([10, 20, 1, 45, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]))
    print(smallest_num([10, 20, 1, 45, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]))