"""
Write a function to check whether the entered number is greater than the elements of the given array.
assert check_greater([1, 2, 3, 4, 5], 4) == False
"""
def check_greater(arr, num):
    """
    :param arr: list of integers
    :param num: integer
    :return: boolean
    """
    return num > max(arr)

assert check_greater([1, 2, 3, 4, 5], 4) == False
assert check_greater([1, 2, 3, 4, 5], 6) == True</s>