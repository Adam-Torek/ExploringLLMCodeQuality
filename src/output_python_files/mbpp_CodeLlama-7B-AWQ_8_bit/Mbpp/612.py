"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""


def merge(lst):
    """
    :param lst: list of lists
    :return: list of two lists
    """
    return [list(zip(*lst))[0], list(zip(*lst))[1]]


if __name__ == '__main__':
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]))
    print(merge([[1, 2], [3, 4], [5, 6]]))
    print(merge([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(merge([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print(merge([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]))
    print(merge([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]))
    print(merge([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21]]))
    print(merge([[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24]]))
    print(merge([[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27]]))
    print(merge([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]))
    print(merge([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]]))
    print(merge([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19,