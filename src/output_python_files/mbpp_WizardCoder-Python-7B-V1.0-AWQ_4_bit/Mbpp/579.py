"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""

def find_dissimilar(t1, t2):
    return tuple(set(t1) - set(t2)) + tuple(set(t2) - set(t1))

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10))) # Output: (3, 6, 7, 10)