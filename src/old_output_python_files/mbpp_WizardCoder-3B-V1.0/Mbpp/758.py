"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""
def unique_sublists(lst):
    sublists = {}
    for sublist in lst:
        sublists[tuple(sublist)] = sublists.get(tuple(sublist), 0) + 1
    return sublists

# Test cases
print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])) # Output: {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}<|endoftext|>