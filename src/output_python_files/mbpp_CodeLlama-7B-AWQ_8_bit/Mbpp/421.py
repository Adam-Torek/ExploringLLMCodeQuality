"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""


def concatenate_tuple(tuple_):
    return '-'.join(str(x) for x in tuple_)


if __name__ == '__main__':
    print(concatenate_tuple(("ID", "is", 4, "UTS")))