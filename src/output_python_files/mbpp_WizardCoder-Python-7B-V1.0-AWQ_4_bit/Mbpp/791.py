"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""

def remove_nested(tup):
    """
    Removes nested tuples from the given tuple
    """
    result = []
    for item in tup:
        if type(item) == tuple:
            result.extend(remove_nested(item))
        else:
            result.append(item)
    return tuple(result)

# Test the function
print(remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)) # True
print(remove_nested((1, (2, (3, 4, (5, 6)), 7, 8, (9, 10))) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # True
print(remove_nested((1, (2, (3, (4, (5, 6), 7), 8), 9, (10, 11))) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) # True
print(remove_nested((1, (2, (3, (4, (5, (6, 7), 8), 9), 10)) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # True
print(remove_nested((1, (2, (3, (4, (5, (6, (7, 8), 9), 10)) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # True
print(remove_nested((1, (2, (3, (4, (5, (6, (7, (8, 9), 10)) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # True
print(remove_nested((1, (2, (3, (4, (5, (6, (7, (8, (9, 10) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # True
print(remove_nested((1, (2, (3, (4, (5, (6, (7, (8, (9, (10, 11) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # True
print(remove_nested((1, (2, (3, (4, (5, (6, (7, (8, (9, (10, (11, 12) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # True
print(remove_nested((1, (2, (3, (4, (5, (6, (7, (8, (9, (10, (11, (12, 13) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # True
print(remove_nested((1, (2, (3, (4, (5, (6, (7, (8, (9, (10, (11, (12, (13, 14) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # True
print(remove_nested((1, (2, (3, (4, (5, (6, (7, (8, (9, (10, (11, (12, (13, (14, 15) == (1, 2, 3, 4, 5,