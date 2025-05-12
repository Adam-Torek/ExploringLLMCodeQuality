def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

def unique_dict(d: dict):
    """Return sorted unique keys in a dictionary
    >>> unique_dict({'a': 1, 'b': 2, 'c': 1, 'd': 3})
    ['a', 'b', 'c', 'd']
    """

def unique_list_dict(l: list, d: dict):
    """Return sorted unique elements in a list and keys in a dictionary
    >>> unique_list_dict([5, 3, 5, 2, 3, 3, 9, 0, 123], {'a': 1, 'b': 2, 'c': 1, 'd': 3})
    [0, 2, 3, 5, 9, 123]
    ['a', 'b', 'c', 'd']
    """

def unique_list_dict_dict(l: list, d: dict, dd: dict):
    """Return sorted unique elements in a list, keys in a dictionary and values in a dictionary
    >>> unique_list_dict_dict([5, 3, 5, 2, 3, 3, 9, 0, 123], {'a': 1, 'b': 2, 'c': 1, 'd': 3}, {'a': 1, 'b': 2, 'c': 1, 'd': 3})
    [0, 2, 3, 5, 9, 123]
    ['a', 'b', 'c', 'd']
    {'a': 1, 'b': 2, 'c': 1, 'd': 3}
    """

def unique_list_dict_dict_dict(l: list, d: dict, dd: dict, ddd: dict):
    """Return sorted unique elements in a list, keys in a dictionary, values in a dictionary and keys in a dictionary
    >>> unique_list_dict_dict_dict([5, 3, 5, 2, 3, 3, 9, 0, 123], {'a': 1, 'b': 2, 'c': 1, 'd': 3}, {'a': 1, 'b': 2, 'c': 1, 'd': 3}, {'a': 1, 'b': 2, 'c': 1, 'd': 3})
    [0, 2, 3, 5, 9, 123]
    ['a', 'b', 'c', 'd']
    {'a': 1, 'b': 2, 'c': 1, 'd': 3}
    {'a': 1, 'b': 2, 'c': 1, 'd': 3}
    """

def unique_list_dict_dict_dict_dict(l: list, d: dict, dd: dict, ddd: dict, dddd: dict):
    """Return sorted unique elements in a list, keys in a dictionary, values in a dictionary, keys in a dictionary and values in a dictionary
    >>> unique_list_dict_dict_dict_dict([5, 3, 5, 2, 3, 3, 9, 0, 123], {'a': 1, 'b': 2, 'c': 1, 'd': 3}, {'a': 1, 'b': 2, 'c': 1, 'd': 3}, {'a': 1, 'b': 2, 'c': 1, 'd': 3}, {'a': 1, 'b': 2, 'c': 1, 'd': 3})
    [0, 2, 3, 5, 9, 123]
    ['a', 'b', 'c', 'd']
    {'a': 1, 'b': 2, 'c': 1, 'd': 3}
    {'a': 1, 'b': 2, 'c': 1, 'd': 3}
    {'a': 1, 'b': 2, 'c': 1, 'd': 3}
    """

def unique