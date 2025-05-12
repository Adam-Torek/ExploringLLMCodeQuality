"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""

def sub_list(lst1, lst2):
    """
    Subtract two lists element-wise
    :param lst1: first list
    :param lst2: second list
    :return: new list with element-wise subtraction
    """
    new_lst = []
    for i in range(len(lst1)):
        new_lst.append(lst1[i] - lst2[i])
    return new_lst


# assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
# print(sub_list([1, 2, 3],[4,5,6]))