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

# Test case
assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
assert min_val([]) is None
assert min_val(['Python', 'Java', 'C++']) == 'C++'
assert min_val([1, 2, 3, 4, 5]) == 1
assert min_val([-1, -2, -3, -4, -5]) == -5
assert min_val([1, 2, 3, 4, 5, 'Python']) == 1
assert min_val(['Python', 3, 2, 4, 5, 'Python']) == 2
assert min_val(['Python', 3, 2, 4, 5, 'Python', 1]) == 1
assert min_val(['Python', 3, 2, 4, 5, 'Python', 1, 'a']) == 1
assert min_val(['Python', 3, 2, 4, 5, 'Python', 1, 'a', 'z']) == 'a'