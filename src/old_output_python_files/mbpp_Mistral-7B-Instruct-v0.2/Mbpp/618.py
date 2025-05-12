"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""
def div_list(lst1, lst2):
    """
    Divides each element of the first list by the corresponding element of the second list.
    :param lst1: list
    :param lst2: list
    :return: list
    """
    return [i/j for i,j in zip(lst1,lst2)]

assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]