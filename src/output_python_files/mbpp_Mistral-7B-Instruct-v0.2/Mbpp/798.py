"""
Write a python function to find the sum of an array.
assert _sum([1, 2, 3]) == 6
"""
def _sum(arr):
    """
    Function to find the sum of an array
    :param arr: list of numbers
    :return: sum of all numbers in the array
    """
    total = 0
    for num in arr:
        total += num
    return total

# Test the function
assert _sum([1, 2, 3]) == 6
assert _sum([0, 0, 0]) == 0
assert _sum([-1, -2, -3]) == -6
assert _sum([]) == 0</s>