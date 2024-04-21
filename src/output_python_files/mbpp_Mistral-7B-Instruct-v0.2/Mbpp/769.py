"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""
def Diff(list1, list2):
    """
    This function returns the difference between two lists.

    Args:
        list1: A list of numbers.
        list2: A list of numbers.

    Returns:
        A list of numbers that are in list1 but not in list2.
    """
    return list(set(list1) - set(list2))

# Test the function
assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30]
assert Diff([1, 2, 3, 4, 5], [2, 3, 5]) == [1]
assert Diff([], [1, 2, 3]) == []
assert Diff([1, 2, 3], [1, 2, 3]) == []</s>