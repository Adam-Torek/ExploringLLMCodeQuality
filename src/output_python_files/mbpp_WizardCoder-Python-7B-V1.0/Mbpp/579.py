"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""

def find_dissimilar(t1, t2):
    return tuple(set(t1) - set(t2)) + tuple(set(t2) - set(t1))

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10))) # Output: (3, 6, 7, 10)
print(find_dissimilar((1, 2, 3, 4), (5, 6, 7, 8))) # Output: (1, 2, 3, 4, 5, 6, 7, 8)
print(find_dissimilar((1, 2, 3), (1, 2, 3, 4))) # Output: (4)
print(find_dissimilar((1, 2, 3), (4, 5, 6))) # Output: (1, 2, 3, 4, 5, 6)
print(find_dissimilar((1, 2, 3), ())) # Output: (1, 2, 3)
print(find_dissimilar((), (1, 2, 3)) # Output: (1, 2, 3)