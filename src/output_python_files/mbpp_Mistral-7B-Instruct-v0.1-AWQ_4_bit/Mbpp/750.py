"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""

def add_tuple(lst, tpl):
    """
    Add a tuple to a list
    """
    lst.append(tuple(tpl))
    return lst

# assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
# print(add_tuple([5, 6, 7], (9, 10)))