"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""


def merge(l):
    return [list(zip(*l))[0], list(zip(*l))[1]]


if __name__ == '__main__':
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y']]))
    print(merge([['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a', 'b'], ['m', 'n'], ['p', 'q'], ['r', 's'], ['t', 'u'], ['v', 'w'], ['x', 'y'], ['a',