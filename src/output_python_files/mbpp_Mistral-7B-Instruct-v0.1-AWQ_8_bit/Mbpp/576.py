"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""

def is_Sub_Array(lst1, lst2):
    """
    :param lst1: list
    :param lst2: list
    :return: True if lst1 is sublist of lst2 else False
    """
    if len(lst1) > len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i:i+len(lst2)] == lst2:
            return True
    return False