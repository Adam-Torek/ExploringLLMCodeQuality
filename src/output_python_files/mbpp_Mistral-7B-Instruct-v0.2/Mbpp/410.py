"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
"""
def min_val(lst):
    if not lst:
        return None
    min_val = lst[0]
    for val in lst:
        if type(val) is int:
            if val < min_val:
                min_val = val
        elif type(val) is str:
            if len(val) < len(min_val):
                min_val = val
    return min_val

# Test the function
assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
assert min_val(['Python', 'three', 2, 4, 5, 'version']) == 'th'
assert min_val([]) is None
assert min_val(['Python', 3, 2, 4, 5, 'version', 0]) == 0
assert min_val(['Python', 3, 2, 4, 5, 'version', 0, '']) == ''
assert min_val(['Python', 3, 2, 4, 5, 'version', 0, 'a', 'z']) == 'a'</s>