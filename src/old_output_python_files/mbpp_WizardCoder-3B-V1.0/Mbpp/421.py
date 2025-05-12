"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""

def concatenate_tuple(t, delimiter='-'):
    return delimiter.join(str(x) for x in t)<|endoftext|>