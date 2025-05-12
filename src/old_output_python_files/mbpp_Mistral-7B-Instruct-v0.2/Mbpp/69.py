"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""
def is_sublist(main_list, sub_list):
    """
    :param main_list: list
    :param sub_list: list
    :return: boolean
    """
    if len(sub_list) > len(main_list):
        return False
    i = 0
    j = 0
    while i < len(main_list) and j < len(sub_list):
        if main_list[i] == sub_list[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(sub_list):
        return True
    else:
        return False

assert is_sublist([2,4,3,5,7],[3,7])==False
assert is_sublist([2,4,3,5,7],[3,5,7])==True
assert is_sublist([1,2,3,4,5],[1,2])==True
assert is_sublist([1,2,3,4,5],[1,3])==False
assert is_sublist([],[])==True
assert is_sublist([],[1])==False