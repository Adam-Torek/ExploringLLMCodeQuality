"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""
def max_val(lst):
    if not lst:
        return None
    max_val = lst[0]
    for i in lst:
        if isinstance(i, (int, float)):
            if i > max_val:
                max_val = i
        elif isinstance(i, str):
            if len(i) > len(max_val):
                max_val = i
    return max_val

assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5
assert max_val(['Python', 3, 2, 4, 5, 'version']) != 'version'
assert max_val([]) is None
assert max_val(['Python', 'three', 2, 4, 5, 'five']) == 'five'
assert max_val(['Python', 'three', 2, 4, 5, 'five']) != 5
assert max_val(['Python', 'three', 2, 4, 5, 'five']) != 3
assert max_val(['Python', 'three', 2, 4, 5, 'five']) != 2
assert max_val(['Python', 'three', 2, 4, 5, 'five']) != 4
assert max_val(['Python', 'three', 2, 4, 5, 'five']) != 'three'
assert max_val(['Python', 'three', 2, 4, 5, 'five']) != 'Python'</s>