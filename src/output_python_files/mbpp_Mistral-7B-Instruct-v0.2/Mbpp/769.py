"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""
def Diff(list1, list2):
    """
    This function returns the difference between two lists.

    Parameters:
    list1 (list): First list
    list2 (list): Second list

    Returns:
    list: Difference between the two lists
    """
    return list(set(list1) - set(list2))

assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30]