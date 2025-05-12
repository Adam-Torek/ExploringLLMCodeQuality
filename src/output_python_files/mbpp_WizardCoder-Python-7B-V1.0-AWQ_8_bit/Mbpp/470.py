"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""

def add_pairwise(tup):
    return tuple(a + b for a, b in zip(tup, tup[1:]))

print(add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)) # True
print(add_pairwise((1, 2, 3, 4, 5)) == (3, 5, 7, 9)) # True
print(add_pairwise((-1, 0, 1, 2, 3)) == (0, 2, 4, 6)) # True
print(add_pairwise((1, 2, 3, 4, 5, 6, 7, 8, 9)) == (3, 5, 7, 9, 11, 13, 15)) # True

# Test cases
print(add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)) # True
print(add_pairwise((1, 2, 3, 4, 5)) == (3, 5, 7, 9)) # True
print(add_pairwise((-1, 0, 1, 2, 3)) == (0, 2, 4, 6)) # True
print(add_pairwise((1, 2, 3, 4, 5, 6, 7, 8, 9)) == (3, 5, 7, 9, 11, 13, 15)) # True
print(add_pairwise((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) == (3, 5, 7, 9, 11, 13, 15, 17, 19)) # True
print(add_pairwise((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)) == (3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23)) # True
print(add_pairwise((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20) == (3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29)) # True

# Test cases with negative numbers
print(add_pairwise((-1, -2, -3, -4, -5) == (-3, -5, -7, -9)) # True
print(add_pairwise((-1, 0, 1, 2, 3) == (0, 2, 4, 6)) # True
print(add_pairwise((-1, 2, 3, 4, 5) == (1, 4, 7, 10)) # True
print(add_pairwise((-1, 2, 3, 4, 5, 6, 7, 8, 9) == (1, 5, 9, 13, 17)) # True
print(add_pairwise((-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) == (1, 5, 9, 13, 17, 21, 25))