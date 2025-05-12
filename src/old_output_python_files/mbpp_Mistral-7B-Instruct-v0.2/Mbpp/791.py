"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""
def remove_nested(input_tuple):
    output_tuple = []
    for element in input_tuple:
        if isinstance(element, tuple):
            output_tuple += remove_nested(element)
        else:
            output_tuple.append(element)
    return tuple(output_tuple)

assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
assert remove_nested((1, 5, 7, (4, 6, 8), 10)) == (1, 5, 7, 10)
assert remove_nested((1, 5, 7, (4, 6), (4, 6))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (4, 6, 8))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (4, 6, 8, 9))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (4, 6, 8, 9), 10)) == (1, 5, 7, 10)
assert remove_nested((1, 5, 7, (4, 6), (4, 6, 8, 9), 10, (4, 6))) == (1, 5, 7, 10)
assert remove_nested((1, 5, 7, (4, 6), (4, 6, 8, 9), 10, (4, 6, 8))) == (1, 5, 7, 10)
assert remove_nested((1, 5, 7, (4, 6), (4, 6, 8, 9), 10, (4, 6, 8, 9))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (4, 6, 8, 9), 10, (4, 6, 8, 9, 11))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (4, 6, 8, 9), 10, (4, 6, 8, 9, 11), (4, 6))) == (1, 5, 7, 10)
assert remove_nested((1, 5, 7, (4, 6), (4, 6, 8, 9), 10, (4, 6, 8, 9, 11), (4, 6), (4, 6))) == (1, 5, 7, 10)
assert remove_nested((1, 5, 7, (4, 6), (4, 6, 8, 9), 10, (4, 6, 8, 9, 11), (4, 6), (4, 6, 8))) == (1, 5, 7, 10)
assert remove_nested((1, 5, 7, (4, 6), (4, 6, 8, 9), 10, (4, 6, 8, 9, 11), (4, 6), (4, 6, 8, 9))) == (1, 5, 7)
assert remove_nested((1, 5, 7, (4, 6), (4, 6, 8, 9), 10, (4, 6, 8, 9, 11), (4, 6), (4, 6, 8, 9, 12))) == (1, 5, 7, 10)
assert remove_nested((1, 5, 7, (4,