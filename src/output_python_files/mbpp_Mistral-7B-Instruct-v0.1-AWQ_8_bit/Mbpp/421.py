"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""

def concatenate_tuple(tuple_data):
    """
    Concatenate each element of tuple by the delimiter.
    """
    delimiter = '-'
    concatenated_tuple = tuple_data[0]
    for item in tuple_data[1:]:
        concatenated_tuple += delimiter + str(item)
    return concatenated_tuple


if __name__ == '__main__':
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'