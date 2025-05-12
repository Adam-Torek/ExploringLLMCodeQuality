"""
Write a function to convert a tuple to a string.
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i','s', 'e','s'))==("exercises")
"""

def tup_string(tup):
    return ''.join(tup)

assert tup_string(('e', 'x', 'e', 'r', 'c', 'i','s', 'e','s'))==("exercises")

"""
Write a function to convert a list to a tuple.
assert list_tuple([1, 3, 5, 6, 8])== (1, 3, 5, 6, 8)
"""

def list_tuple(lst):
    return tuple(lst)

assert list_tuple([1, 3, 5, 6, 8])== (1, 3, 5, 6, 8)

"""
Write a function to convert a list to a dictionary.
assert list_dict([1, 2, 3, 4, 5])== {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

def list_dict(lst):
    return {i: i**2 for i in lst}

assert list_dict([1, 2, 3, 4, 5])== {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""
Write a function to convert a dictionary to a tuple.
assert dict_tuple({1: 1, 2: 4, 3: 9, 4: 16, 5: 25})== ((1, 1), (2, 4), (3, 9), (4, 16), (5, 25))
"""

def dict_tuple(dct):
    return tuple(dct.items())

assert dict_tuple({1: 1, 2: 4, 3: 9, 4: 16, 5: 25})== ((1, 1), (2, 4), (3, 9), (4, 16), (5, 25))

"""
Write a function to convert a tuple to a dictionary.
assert tuple_dict((('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)))== {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
"""

def tuple_dict(tup):
    return dict(tup)

assert tuple_dict((('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)))== {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

"""
Write a function to convert a dictionary to a list.
assert dict_list({1: 1, 2: 4, 3: 9, 4: 16, 5: 25})== [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
"""

def dict_list(dct):
    return list(dct.items())

assert dict_list({1: 1, 2: 4, 3: 9, 4: 16, 5: 25})== [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

"""
Write a function to convert a list to a set.
assert list_set([1, 2, 3, 4, 5])== {1, 2, 3, 4, 5}
"""

def list_set(lst):
    return set(lst)

assert list_set([1, 2, 3, 4, 5])== {1, 2, 3, 4, 5}

"""
Write a function to convert a set to a list.
assert set_list({1, 2, 3, 4, 5})== [1, 2, 3, 4