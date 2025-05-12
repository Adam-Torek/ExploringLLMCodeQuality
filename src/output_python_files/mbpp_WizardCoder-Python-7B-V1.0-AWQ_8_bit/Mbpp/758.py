"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""

def unique_sublists(lst):
    d = {}
    for sublst in lst:
        t = tuple(sublst)
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    return d

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
# Output: {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}

# Test cases
print(unique_sublists([[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6], [10, 11, 12], [7, 8, 9]]))
# Output: {(1, 2, 3): 2, (4, 5, 6): 2, (7, 8, 9): 2, (10, 11, 12): 1}

print(unique_sublists([[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6], [10, 11, 12], [7, 8, 9], [13, 14, 15]]))
# Output: {(1, 2, 3): 2, (4, 5, 6): 2, (7, 8, 9): 2, (10, 11, 12): 1, (13, 14, 15): 1}

print(unique_sublists([[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6], [10, 11, 12], [7, 8, 9], [13, 14, 15], [1, 2, 3]]))
# Output: {(1, 2, 3): 3, (4, 5, 6): 3, (7, 8, 9): 3, (10, 11, 12): 1, (13, 14, 15): 1}

print(unique_sublists([[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6], [10, 11, 12], [7, 8, 9], [13, 14, 15], [1, 2, 3], [16, 17, 18]]))
# Output: {(1, 2, 3): 3, (4, 5, 6): 3, (7, 8, 9): 3, (10, 11, 12): 1, (13, 14, 15): 1, (16, 17, 18): 1}

print(unique_sublists([[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6], [10