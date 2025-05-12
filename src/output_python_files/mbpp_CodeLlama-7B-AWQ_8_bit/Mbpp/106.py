"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""


def add_lists(list_to_add, tuple_to_add):
    """
    Adds the list to the tuple.
    :param list_to_add: list to add
    :param tuple_to_add: tuple to add
    :return: tuple with list added
    """
    return tuple_to_add + tuple(list_to_add)


if __name__ == '__main__':
    print(add_lists([5, 6, 7], (9, 10)))
    print(add_lists([5, 6, 7], (9, 10, 11)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13, 14)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13, 14, 15)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)))
    print(add_lists([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)))
    print(add_lists([5, 6, 7], (