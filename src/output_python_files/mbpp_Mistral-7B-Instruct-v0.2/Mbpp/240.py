"""
Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
"""
def replace_list(lst1, lst2):
    """
    Replaces the last element of the first list with the elements of the second list
    :param lst1: list
    :param lst2: list
    :return: list
    """
    lst1[-1] = lst2
    return lst1</s>