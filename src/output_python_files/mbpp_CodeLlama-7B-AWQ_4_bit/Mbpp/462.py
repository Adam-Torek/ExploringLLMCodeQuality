"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""


def combinations_list(list_):
    """
    Write a function to find all possible combinations of the elements of a given list.
    """
    if not list_:
        return []
    if len(list_) == 1:
        return [list_]
    else:
        return [list_[:i] + list_[i + 1:] for i in range(len(list_))] + combinations_list(list_[1:])


if __name__ == '__main__':
    print(combinations_list(['orange', 'red', 'green', 'blue']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'black']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'black', 'white']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'black', 'white', 'gray']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'black', 'white', 'gray', 'pink']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'black', 'white', 'gray', 'pink', 'brown']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'black', 'white', 'gray', 'pink', 'brown', 'orange']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'black', 'white', 'gray', 'pink', 'brown', 'orange', 'red']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'black', 'white', 'gray', 'pink', 'brown', 'orange', 'red', 'green']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'black', 'white', 'gray', 'pink', 'brown', 'orange', 'red', 'green', 'blue']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'black', 'white', 'gray', 'pink', 'brown', 'orange', 'red', 'green', 'blue', 'yellow']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'black', 'white', 'gray', 'pink', 'brown', 'orange', 'red', 'green', 'blue', 'yellow', 'purple']))
    print(combinations_list(['orange', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'black', 'white', 'gray', 'pink', 'brown', 'orange', 'red', 'green', 'blue', '