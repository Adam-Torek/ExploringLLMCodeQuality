"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""

def dict_depth(d):
    if not d:
        return 0
    return 1 + max(dict_depth(d[k]) for k in d)

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
assert dict_depth({'a':1, 'b': {'c': {'d': {}}