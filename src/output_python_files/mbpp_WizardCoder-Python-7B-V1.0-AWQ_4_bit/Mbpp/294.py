"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""

def max_val(lst):
    max_val = lst[0]
    for i in lst:
        if type(i) == str:
            continue
        elif i > max_val:
            max_val = i
    return max_val

print(max_val(['Python', 3, 2, 4, 5, 'version'])) # Output: 5