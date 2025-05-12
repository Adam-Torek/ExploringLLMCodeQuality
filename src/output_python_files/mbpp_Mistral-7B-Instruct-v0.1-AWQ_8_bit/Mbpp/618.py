"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""

def div_list(lst1, lst2):
    """
    Divide two lists element wise.
    :param lst1: first list
    :param lst2: second list
    :return: list of division results
    """
    result = []
    for i in range(len(lst1)):
        result.append(lst1[i]/lst2[i])
    return result

# assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
print(div_list([4,5,6],[1, 2, 3]))