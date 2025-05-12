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
Write a function to convert a list to a set.
assert list_set([1, 3, 5, 6, 8])== {1, 3, 5, 6, 8}
"""

def list_set(lst):
    return set(lst)

assert list_set([1, 3, 5, 6, 8])== {1, 3, 5, 6, 8}

"""
Write a function to convert a set to a list.
assert set_list({1, 3, 5, 6, 8})== [1, 3, 5, 6, 8]
"""

def set_list(st):
    return list(st)

assert set_list({1, 3, 5, 6, 8})== [1, 3, 5, 6, 8]

"""
Write a function to convert a set to a tuple.
assert set_tuple({1, 3, 5, 6, 8})== (1, 3, 5, 6, 8)
"""

def set_tuple(st):
    return tuple(st)

assert set_tuple({1, 3, 5, 6, 8})== (1, 3, 5, 6, 8)

"""
Write a function to convert a tuple to a set.
assert tuple_set((1, 3, 5, 6, 8))== {1, 3, 5, 6, 8}
"""

def tuple_set(tup):
    return set(tup)

assert tuple_set((1, 3, 5, 6, 8))== {1, 3, 5, 6, 8}

"""
Write a function to convert a tuple to a list.
assert tuple_list((1, 3, 5, 6, 8))== [1, 3, 5, 6, 8]
"""

def tuple_list(tup):
    return list(tup)

assert tuple_list((1, 3, 5, 6, 8))== [1, 3, 5, 6, 8]

"""
Write a function to convert a list to a dictionary.
assert list_dict([1, 3, 5, 6, 8])== {1: None, 3: None, 5: None, 6: None, 8: None}
"""

def list_dict(lst):
    return {i: None for i in lst}

assert list_dict([1, 3, 5, 6, 8])== {1: None, 3: None, 5: None, 6: None, 8: None}

"""
Write a function to convert a set to a dictionary.
assert set_dict({1, 3, 5, 6, 8})== {1: None, 3: None, 5: None, 6: None, 8: None}
"""

def set_dict(st):
    return {i: None for i in st}

assert set_dict({1, 3, 5, 6, 8})== {1: None, 3: None, 5