"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""

def div_list(lst1, lst2):
    """
    Divide two lists element wise.
    :param lst1: first list
    :param lst2: second list
    :return: list of division of corresponding elements of lst1 and lst2
    """
    if len(lst1) != len(lst2):
        raise ValueError("Lists must have the same number of elements.")
    else:
        return [lst1[i] / lst2[i] for i in range(len(lst1))]

# Test the function
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]