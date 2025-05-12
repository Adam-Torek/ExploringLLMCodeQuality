"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""


def add_lists(list_to_add, tuple_to_add):
    """
    Adds the list to the tuple.
    :param list_to_add: list to add
    :param tuple_to_add: tuple to add
    :return: tuple with the list added
    """
    return tuple_to_add + tuple(list_to_add)


if __name__ == '__main__':
    print(add_lists([5, 6, 7], (9, 10)))
    print(add_lists([1, 2, 3], (4, 5, 6)))
    print(add_lists([1, 2, 3], (4, 5)))
    print(add_lists([1, 2, 3], (4,)))
    print(add_lists([1, 2, 3], ()))
    print(add_lists([1, 2, 3], (4, 5, 6, 7, 8, 9, 10)))
    print(add_lists([1, 2, 3], (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)))
    print(add_lists([1, 2, 3], (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,