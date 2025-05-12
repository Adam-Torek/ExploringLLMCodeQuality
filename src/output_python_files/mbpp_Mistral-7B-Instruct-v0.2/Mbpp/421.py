"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""
def concatenate_tuple(tuple_):
    """
    Concatenate each element of tuple by '-' delimiter
    :param tuple_: tuple
    :return: str
    """
    return '-'.join(map(str, tuple_))

assert concatenate_tuple(("ID", "is", 4, "UTS")) == 'ID-is-4-UTS'