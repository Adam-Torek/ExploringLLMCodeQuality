"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""
def sub_list(list1, list2):
    """
    Subtracts two lists element-wise and returns the new list
    :param list1: list
    :param list2: list
    :return: list
    """
    result = []
    for i in range(len(list1)):
        result.append(list1[i] - list2[i])
    return result

assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]