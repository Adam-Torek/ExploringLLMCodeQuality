"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""

def sub_list(lst1, lst2):
    """
    This function takes two lists as input and returns the element-wise subtraction of the two lists.
    """
    result = []
    for i in range(len(lst1)):
        result.append(lst1[i] - lst2[i])
    return result

# Test the function
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]