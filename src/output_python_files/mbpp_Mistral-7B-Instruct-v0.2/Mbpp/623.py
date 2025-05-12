"""
Write a function to compute the n-th power of each number in a list.
assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
def nth_nums(nums, n):
    """
    :param nums: list of numbers
    :param n: integer, power to raise each number to
    :return: list of numbers raised to the n-th power
    """
    return [num ** n for num in nums]

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 2
    assert nth_nums(nums, n) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print("Test passed!")