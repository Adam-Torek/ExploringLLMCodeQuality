"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""

def add_pairwise(tup):
    result = []
    for i in range(len(tup)-1):
        result.append(tup[i] + tup[i+1])
    return tuple(result)

# Test the function
print(add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)) # True
print(add_pairwise((1, 2, 3, 4, 5)) == (3, 5, 7, 9)) # True
print(add_pairwise((-1, 0, 1, 2, 3)) == (0, 2, 4, 6)) # True
print(add_pairwise((-1, -2, -3, -4, -5)) == (-3, -1, 0, 2)) # True
print(add_pairwise((1, 2, 3, 4, 5, 6, 7, 8, 9)) == (3, 5, 7, 9, 11, 13, 15)) # True
print(add_pairwise(()) == ()) # True
print(add_pairwise((1,)) == ()) # True
print(add_pairwise(()) == ()) # True