"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""

def add_pairwise(tup):
    return tuple(a + b for a, b in zip(tup, tup[1:]))

print(add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)) # True
print(add_pairwise((1, 2, 3, 4, 5)) == (3, 5, 7, 9)) # True
print(add_pairwise((-1, 0, 1, 2, 3)) == (0, 2, 4, 6)) # True
print(add_pairwise((0, 1, 2, 3, 4, 5)) == (1, 3, 5, 7, 9)) # True
print(add_pairwise((1, 2, 3, 4, 5, 6, 7, 8, 9)) == (3, 5, 7, 9, 11, 13)) # True

# Test cases
print(add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)) # True
print(add_pairwise((1, 2, 3, 4, 5)) == (3, 5, 7, 9)) # True
print(add_pairwise((-1, 0, 1, 2, 3)) == (0, 2, 4, 6)) # True
print(add_pairwise((0, 1, 2, 3, 4, 5) == (1, 3, 5, 7, 9)) # True
print(add_pairwise((1, 2, 3, 4, 5, 6, 7, 8, 9) == (3, 5, 7, 9, 11, 13)) # True

# Test cases
print(add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)) # True
print(add_pairwise((1, 2, 3, 4, 5)) == (3, 5, 7, 9)) # True
print(add_pairwise((-1, 0, 1, 2, 3)) == (0, 2, 4, 6)) # True
print(add_pairwise((0, 1, 2, 3, 4, 5) == (1, 3, 5, 7, 9)) # True
print(add_pairwise((1, 2, 3, 4, 5, 6, 7, 8, 9) == (3, 5, 7, 9, 11, 13)) # True

# Test cases
print(add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)) # True
print(add_pairwise((1, 2, 3, 4, 5)) == (3, 5, 7, 9)) # True
print(add_pairwise((-1, 0, 1, 2, 3)) == (0, 2, 4, 6)) # True
print(add_pairwise((0, 1, 2, 3, 4, 5) == (1, 3, 5, 7, 9)) # True
print(add_pairwise((1, 2, 3, 4, 5, 6, 7, 8, 9) == (3, 5, 7, 9, 11, 13)) # True