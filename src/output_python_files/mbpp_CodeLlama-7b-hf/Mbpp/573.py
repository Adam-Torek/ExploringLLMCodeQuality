"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""


def unique_product(nums):
    """
    :param nums: list of numbers
    :return: product of unique numbers
    """
    nums.sort()
    product = 1
    for i in range(len(nums)):
        if i == 0:
            product = nums[i]
        elif nums[i] != nums[i - 1]:
            product *= nums[i]
    return product


if __name__ == '__main__':
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 10]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 10, 10]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 10, 10, 10]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 10, 10, 10, 10]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 10, 10, 10, 10, 10]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 10, 10, 10, 10, 10, 10]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 10, 10, 10, 10, 10, 10, 10]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    print