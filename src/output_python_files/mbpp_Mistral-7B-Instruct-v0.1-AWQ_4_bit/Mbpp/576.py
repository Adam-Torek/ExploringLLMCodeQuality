"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""

def is_Sub_Array(lst1, lst2):
    """
    :param lst1:
    :param lst2:
    :return:
    """
    if len(lst1) < len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i:i+len(lst2)] == lst2:
            return True
    return False


# assert is_Sub_Array([1,4,3,5],[1,2]) == False
# assert is_Sub_Array([1,4,3,5],[1,2,3]) == True
# assert is_Sub_Array([1,4,3,5],[1,2,3,4]) == True
# assert is_Sub_Array([1,4,3,5],[1,2,3,4,5]) == False