"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""

def new_tuple(lst, s):
    """
    Create a new tuple from the given list and string.
    """
    return tuple(lst) + tuple([s])

assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')