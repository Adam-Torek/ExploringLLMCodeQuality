"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""


def combinations_list(list_):
    """
    Write a function to find all possible combinations of the elements of a given list.
    :param list_: list of elements
    :return: list of all possible combinations
    """
    if not list_:
        return []
    else:
        return [list_[:i] + list_[i + 1:] for i in range(len(list_))]


if __name__ == '__main__':
    print(combinations_list(['orange', 'red', 'green', 'blue']))
    print(combinations_list(['a', 'b', 'c']))
    print(combinations_list(['a', 'b', 'c', 'd']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']))
    print(combinations_list(['a', 'b', 'c', 'd', 'e', 'f', 'g