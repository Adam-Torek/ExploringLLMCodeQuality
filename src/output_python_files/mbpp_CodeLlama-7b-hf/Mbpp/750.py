"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""


def add_tuple(list_: list, tuple_: tuple) -> list:
    """
    Adds the given tuple to the given list.
    :param list_: The list to add the tuple to.
    :param tuple_: The tuple to add to the list.
    :return: The list with the tuple added.
    """
    list_.extend(tuple_)
    return list_


if __name__ == '__main__':
    print(add_tuple([5, 6, 7], (9, 10)))
    print(add_tuple([5, 6, 7], (9, 10, 11)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12, 13)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)))
    print(add_tuple([5, 6, 7], (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)))
    print(add_tuple([5, 6, 7], (9, 10, 1