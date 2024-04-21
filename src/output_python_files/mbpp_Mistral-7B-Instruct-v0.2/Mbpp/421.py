"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""
def concatenate_tuple(tuple_input):
    """
    Concatenates each element of tuple by the delimiter '-'
    :param tuple_input: tuple
    :return: str
    """
    delimiter = '-'
    return '-'.join(map(str, tuple_input))

assert concatenate_tuple(("ID", "is", 4, "UTS")) == 'ID-is-4-UTS'</s>