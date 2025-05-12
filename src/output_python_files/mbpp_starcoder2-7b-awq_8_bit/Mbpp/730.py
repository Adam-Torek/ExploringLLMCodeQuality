"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""

def consecutive_duplicates(lst):
    """
    >>> consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    """
    new_lst = []
    for i in range(len(lst)):
        if lst[i]!= lst[i-1]:
            new_lst.append(lst[i])
    return new_lst

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day03/02_list_to_dict.py
"""
Write a function that takes a list of tuples and returns a dictionary.
assert list_to_dict([('a', 1), ('b', 2), ('c', 3)]) == {'a': 1, 'b': 2, 'c': 3}
"""

def list_to_dict(lst):
    """
    >>> list_to_dict([('a', 1), ('b', 2), ('c', 3)])
    {'a': 1, 'b': 2, 'c': 3}
    """
    new_dict = {}
    for i in range(len(lst)):
        new_dict[lst[i][0]] = lst[i][1]
    return new_dict

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day03/01_dict_to_list.py
"""
Write a function that takes a dictionary and returns a list of tuples.
assert dict_to_list({'a': 1, 'b': 2, 'c': 3}) == [('a', 1), ('b', 2), ('c', 3)]
"""

def dict_to_list(dct):
    """
    >>> dict_to_list({'a': 1, 'b': 2, 'c': 3})
    [('a', 1), ('b', 2), ('c', 3)]
    """
    new_list = []
    for key in dct:
        new_list.append((key, dct[key]))
    return new_list

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day03/03_dict_to_list_of_lists.py
"""
Write a function that takes a dictionary and returns a list of lists.
assert dict_to_list_of_lists({'a': 1, 'b': 2, 'c': 3}) == [['a', 1], ['b', 2], ['c', 3]]
"""

def dict_to_list_of_lists(dct):
    """
    >>> dict_to_list_of_lists({'a': 1, 'b': 2, 'c': 3})
    [['a', 1], ['b', 2], ['c', 3]]
    """
    new_list = []
    for key in dct:
        new_list.append([key, dct[key]])
    return new_list

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day03/04_list_of_lists_to_dict.py
"""
Write a function that takes a list of lists and returns a dictionary.
assert list_of_lists_to_dict([['a', 1], ['b', 2], ['c', 3]]) == {'a': 1, 'b': 2, 'c': 3}
"""

def list_of_lists_to_dict(lst):
    """
    >>> list_of_lists_to_dict([['a', 1], ['b', 2], ['c', 3]])
    {'