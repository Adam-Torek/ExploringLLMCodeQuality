"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""

def add_tuple(lst, tpl):
    """
    This function takes a list and a tuple as input and returns the list with the tuple added.
    """
    lst.append(tpl)
    return lst

# Test the function
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]