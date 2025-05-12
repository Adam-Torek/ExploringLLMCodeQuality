"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""


def sort_sublists(lists):
    """
    :param lists: list of lists
    :return: list of lists
    """
    return [sorted(sublist) for sublist in lists]


if __name__ == '__main__':
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['red', 'blue']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['red', 'blue'], ['yellow', 'purple']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['red', 'blue'], ['yellow', 'purple'], ['red', 'green', 'blue']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['red', 'blue'], ['yellow', 'purple'], ['red', 'green', 'blue'], ['red', 'green', 'blue', 'yellow']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['red', 'blue'], ['yellow', 'purple'], ['red', 'green', 'blue'], ['red', 'green', 'blue', 'yellow'], ['red', 'green', 'blue', 'yellow', 'purple']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['red', 'blue'], ['yellow', 'purple'], ['red', 'green', 'blue'], ['red', 'green', 'blue', 'yellow'], ['red', 'green', 'blue', 'yellow', 'purple'], ['red', 'green', 'blue', 'yellow', 'purple', 'orange']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['red', 'blue'], ['yellow', 'purple'], ['red', 'green', 'blue'], ['red', 'green', 'blue', 'yellow'], ['red', 'green', 'blue', 'yellow', 'purple'], ['red', 'green', 'blue', 'yellow', 'purple', 'orange'], ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['red', 'blue'], ['yellow', 'purple'], ['red', 'green', 'blue'], ['red', 'green', 'blue', 'yellow'], ['red', 'green', 'blue', 'yellow', 'purple'], ['red', 'green', 'blue', 'yellow', 'purple', 'orange'], ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black'], ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black', 'white']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['red', 'blue'], ['yellow', 'purple'], ['red', 'green', 'blue'], ['red', 'green', 'blue', 'yellow'], ['red', 'green', 'blue', 'yellow', 'purple'], ['red', 'green', 'blue', 'yellow', 'purple', 'orange'], ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black'], ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black', 'white'], ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black', 'white', '