"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""


def new_tuple(list_of_str, str_of_str):
    """
    Create a new tuple from the given string and list.
    :param list_of_str: list of strings
    :param str_of_str: string of strings
    :return: tuple
    """
    return tuple(list_of_str + [str_of_str])


if __name__ == '__main__':
    print("Example:")
    print(new_tuple(["WEB", "is"], "best"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
    assert new_tuple(["WEB", "is", "the"], "best") == ('WEB', 'is', 'the', 'best')
    assert new_tuple(["WEB", "is", "the", "best"], "way") == ('WEB', 'is', 'the', 'best', 'way')
    assert new_tuple(["WEB", "is", "the", "best", "way"], "to") == ('WEB', 'is', 'the', 'best', 'way', 'to')
    assert new_tuple(["WEB", "is", "the", "best", "way", "to"], "learn") == ('WEB', 'is', 'the', 'best', 'way', 'to',
                                                                              'learn')
    assert new_tuple(["WEB", "is", "the", "best", "way", "to", "learn"], "python") == ('WEB', 'is', 'the', 'best', 'way',
                                                                                       'to', 'learn', 'python')
    assert new_tuple(["WEB", "is", "the", "best", "way", "to", "learn", "python"], "programming") == ('WEB', 'is', 'the',
                                                                                                       'best', 'way',
                                                                                                       'to', 'learn',
                                                                                                       'python',
                                                                                                       'programming')
    assert new_tuple(["WEB", "is", "the", "best", "way", "to", "learn", "python", "programming"], "in") == ('WEB', 'is',
                                                                                                           'the', 'best',
                                                                                                           'way', 'to',
                                                                                                           'learn',
                                                                                                           'python',
                                                                                                           'programming',
                                                                                                           'in')
    assert new_tuple(["WEB", "is", "the", "best", "way", "to", "learn", "python", "programming", "in"], "2018") == ('WEB',
                                                                                                                 'is',
                                                                                                                 'the',
                                                                                                                 'best',
                                                                                                                 'way',
                                                                                                                 'to',
                                                                                                                 'learn',
                                                                                                                 'python',
                                                                                                                 'programming',
                                                                                                                 'in',
                                                                                                                 '2018')
    assert new_tuple(["WEB", "is", "the", "best", "way", "to", "learn", "python", "programming", "in", "2018"],
                     "a") == ('WEB', 'is', 'the', 'best', 'way', 'to', 'learn', 'python', 'programming', 'in', '2018',
                               'a')
    assert new_tuple(["WEB", "is", "the", "best", "way", "to", "learn", "python", "programming", "in", "2018", "a"],
                     "beginner") == ('WEB', 'is', 'the', 'best', 'way