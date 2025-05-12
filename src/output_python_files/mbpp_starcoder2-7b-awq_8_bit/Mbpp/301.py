"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""

def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    return 1 + max(dict_depth(v) for v in d.values())

assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'