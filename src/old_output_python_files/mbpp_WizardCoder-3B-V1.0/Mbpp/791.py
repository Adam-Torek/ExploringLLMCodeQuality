"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""

def remove_nested(t):
    if isinstance(t, tuple):
        return tuple(remove_nested(x) for x in t)
    else:
        return t

# Test
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)<|endoftext|>