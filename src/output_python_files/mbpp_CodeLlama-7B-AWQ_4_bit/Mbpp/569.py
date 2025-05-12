"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""


def sort_sublists(lst):
    """
    Sort each sublist of strings in a given list of lists.
    :param lst: list of lists
    :return: list of lists
    """
    return [sorted(sublist) for sublist in lst]


if __name__ == '__main__':
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['green', 'orange', 'black', 'white']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['green', 'orange', 'black', 'white'], ['green', 'orange', 'black', 'white', 'black']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['green', 'orange', 'black', 'white'], ['green', 'orange', 'black', 'white', 'black'], ['green', 'orange', 'black', 'white', 'black', 'orange']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['green', 'orange', 'black', 'white'], ['green', 'orange', 'black', 'white', 'black'], ['green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange', 'green', 'orange', 'black', 'white', 'black', 'orange']]))
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'], ['green', 'orange', 'black', 'white'], ['green', 'orange', 'black', 'white', 'black'], ['green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange', 'green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange', 'green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange', 'green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange', 'green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange', 'green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange', 'green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange', 'green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange', 'green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange', 'green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange', 'green', 'orange', 'black', 'white', 'black', 'orange'], ['green', 'orange', 'black', 'white', 'black', 'orange', '