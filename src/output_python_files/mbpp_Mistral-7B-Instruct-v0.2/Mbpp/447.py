"""
Write a function to find cubes of individual elements in a list.
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""
def cube_nums(nums):
    """
    Function to find cubes of individual elements in a list
    :param nums: list of numbers
    :return: list of cubes of individual elements in the list
    """
    result = []
    for num in nums:
        result.append(num ** 3)
    return result

# Test the function
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
print("Test passed!")</s>