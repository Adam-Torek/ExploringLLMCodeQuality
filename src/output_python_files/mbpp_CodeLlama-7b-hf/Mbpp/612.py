"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""


def merge(list_of_lists):
    """
    :param list_of_lists: list of lists
    :return: list of two lists
    """
    return [list(zip(*list_of_lists))[0], list(zip(*list_of_lists))[1]]


if __name__ == '__main__':
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['z', 'y']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['z', 'y'], ['a', 'b']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['z', 'y'], ['a', 'b'], ['a', 'b']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['z', 'y'], ['a', 'b'], ['a', 'b'], ['a', 'b']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['z', 'y'], ['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['z', 'y'], ['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['z', 'y'], ['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['z', 'y'], ['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p',