"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""
def sub_list(list1, list2):
    """
    Subtracts two lists element-wise and returns a new list with the differences.
    :param list1: A list of numbers
    :param list2: A list of numbers of the same length as list1
    :return: A new list with the differences between the corresponding elements of list1 and list2
    """
    if len(list1) != len(list2):
        raise ValueError("The lists must have the same length.")

    result = []
    for i in range(len(list1)):
        result.append(list1[i] - list2[i])

    return result