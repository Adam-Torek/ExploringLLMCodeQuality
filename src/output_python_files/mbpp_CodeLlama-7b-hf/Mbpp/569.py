"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""


def sort_sublists(list_of_lists):
    """
    Sorts each sublist of strings in a given list of lists.
    :param list_of_lists: list of lists
    :return: list of lists
    """
    for i in range(len(list_of_lists)):
        list_of_lists[i].sort()
    return list_of_lists


if __name__ == '__main__':
    print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))
