"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""

def is_sublist(lst, sublist):
    """
    :param lst: list
    :param sublist: sublist
    :return: True if sublist is present in lst else False
    """
    if len(sublist) == 0:
        return True
    for i in range(len(lst)-len(sublist)+1):
        if lst[i:i+len(sublist)] == sublist:
            return True
    return False