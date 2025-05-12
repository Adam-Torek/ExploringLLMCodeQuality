"""
Write a python function to find the length of the smallest list in a list of lists.
assert Find_Min_Length([[1],[1,2]]) == 1
"""
def Find_Min_Length(lst):
    """
    This function takes a list of lists as an argument and returns the length of the smallest list in the list.
    """
    if not lst:
        raise ValueError("List is empty")
    return min([len(i) for i in lst])

# Test the function
assert Find_Min_Length([[1],[1,2]]) == 1
assert Find_Min_Length([[1,2],[3,4,5]]) == 2
assert Find_Min_Length([]) == ValueError("List is empty")
assert Find_Min_Length([[1,2,3],[1,2],[1]]) == 1
assert Find_Min_Length([[1,2],[1,2],[1,2]]) == 2
assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2