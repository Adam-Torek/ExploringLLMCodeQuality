"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""

def check_Consecutive(lst):
    """
    :param lst: list of integers
    :return: True if the list contains consecutive numbers, False otherwise
    """
    if len(lst) < 2:
        return False
    for i in range(1,len(lst)):
        if lst[i] - lst[i-1] != 1:
            return False
    return True