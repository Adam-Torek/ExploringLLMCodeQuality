"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""


def add_tuple(list_of_tuples, tuple_to_add):
    """
    Adds the given tuple to the given list.
    :param list_of_tuples: list of tuples
    :param tuple_to_add: tuple to add
    :return: list of tuples
    """
    list_of_tuples.append(tuple_to_add)
    return list_of_tuples


if __name__ == '__main__':
    print("Example:")
    print(add_tuple([5, 6, 7], (9, 10)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
    assert add_tuple([5, 6, 7], (9, 10, 11)) == [5, 6, 7, 9, 10, 11]
    assert add_tuple([5, 6, 7], (9, 10, 11, 12)) == [5, 6, 7, 9, 10, 11, 12]
    assert add_tuple([5, 6, 7], (9, 10, 11, 12, 13)) == [5, 6, 7, 9, 10, 11, 12, 13]
    assert add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14)) == [5, 6, 7, 9, 10, 11, 12, 13, 14]
    assert add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15)) == [5, 6, 7, 9, 10, 11, 12, 13, 14, 15]
    assert add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16)) == [5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]
    assert add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17)) == [5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    assert add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18)) == [5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    assert add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)) == [5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17