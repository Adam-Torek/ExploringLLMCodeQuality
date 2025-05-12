"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""
def remove_nested(tuple_to_remove):
    result = []
    i = 0
    while i < len(tuple_to_remove):
        if isinstance(tuple_to_remove[i], tuple):
            result += remove_nested(tuple_to_remove[i])
        elif tuple_to_remove[i] != object:
            result.append(tuple_to_remove[i])
        i += 1
    return tuple(result)

assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
assert remove_nested((1, 5, 7, (4, 6, 7), 10)) == (1, 5, 7, 10)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3), 10)) == (1, 5, 7, 10)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3), (4, 6))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3), (4, 6, 7))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3), (4, 6, 7, 8))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3), (4, 6, 7, 8), (4, 6))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3), (4, 6, 7, 8), (4, 6, 9))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3), (4, 6, 7, 8), (4, 6, 9), (4, 6))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3), (4, 6, 7, 8), (4, 6, 9), (4, 6, 10))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3), (4, 6, 7, 8), (4, 6, 9), (4, 6, 10), (4, 6))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3), (4, 6, 7, 8), (4, 6, 9), (4, 6, 10), (4, 6, 11))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3), (4, 6, 7, 8), (4, 6, 9), (4, 6, 10), (4, 6, 11), (4, 6))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (1, 2, 3), (4, 6, 7, 8), (4, 6, 9