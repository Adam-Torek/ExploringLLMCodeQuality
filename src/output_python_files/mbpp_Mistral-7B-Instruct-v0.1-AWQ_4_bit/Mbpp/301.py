"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""

def dict_depth(d):
    """
    Returns the depth of a dictionary.
    """
    if type(d) == dict:
        count = 0
        for k, v in d.items():
            if type(v) == dict:
                count += 1 + dict_depth(v)
            else:
                count += 1
        return count
    else:
        return 0

assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4