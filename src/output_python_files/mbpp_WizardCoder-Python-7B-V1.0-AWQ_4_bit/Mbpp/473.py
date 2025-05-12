"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""

def tuple_intersection(t1, t2):
    t1_set = set(tuple(sorted(t)) for t in t1)
    t2_set = set(tuple(sorted(t)) for t in t2)
    return t1_set.intersection(t2_set)

# Testing the function
print(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)])) # Output: {(4, 5), (3, 4), (5, 6)}