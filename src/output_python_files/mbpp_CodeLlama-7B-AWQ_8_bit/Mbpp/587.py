"""
Write a function to convert a list to a tuple.
assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
"""


def list_tuple(lst):
    return tuple(lst)


def test_list_tuple():
    assert list_tuple([5, 10, 7, 4, 15, 3]) == (5, 10, 7, 4, 15, 3)


if __name__ == '__main__':
    test_list_tuple()