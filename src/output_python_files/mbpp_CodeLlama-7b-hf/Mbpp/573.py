"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""


def unique_product(nums):
    """
    :param nums: list of numbers
    :return: product of unique numbers
    """
    # sort the list
    nums.sort()
    # initialize the product
    product = 1
    # iterate over the list
    for i in range(len(nums)):
        # if the number is not equal to the next number
        if nums[i] != nums[i + 1]:
            # multiply the product with the number
            product *= nums[i]
    return product


if __name__ == '__main__':
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40]))
    print(unique_product([10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10, 20, 30, 40, 20, 50, 60, 40, 10,