"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""

def dict_depth(d):
    """
    Returns the depth of a dictionary.
    """
    if type(d) == dict:
        return 1 + max(map(dict_depth, d.values()))
    else:
        return 0

assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4