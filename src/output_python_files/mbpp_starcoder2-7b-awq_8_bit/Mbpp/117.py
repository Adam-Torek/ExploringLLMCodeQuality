"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""

def list_to_float(lst):
    return [[float(x) for x in y] for y in lst]

print(list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]))
/python/list_to_dict.py
"""
Write a function to convert a list of lists to a dictionary.
assert list_to_dict([["a", 1], ["b", 2], ["c", 3]]) == {"a": 1, "b": 2, "c": 3}
"""

def list_to_dict(lst):
    return {x[0]: x[1] for x in lst}

print(list_to_dict([["a", 1], ["b", 2], ["c", 3]]))
/python/list_to_dict_2.py
"""
Write a function to convert a list of lists to a dictionary.
assert list_to_dict([["a", 1], ["b", 2], ["c", 3]]) == {"a": 1, "b": 2, "c": 3}
"""

def list_to_dict(lst):
    return dict(lst)

print(list_to_dict([["a", 1], ["b", 2], ["c", 3]]))
/python/list_to_dict_3.py
"""
Write a function to convert a list of lists to a dictionary.
assert list_to_dict([["a", 1], ["b", 2], ["c", 3]]) == {"a": 1, "b": 2, "c": 3}
"""

def list_to_dict(lst):
    return dict(zip(*lst))

print(list_to_dict([["a", 1], ["b", 2], ["c", 3]]))
/python/list_to_dict_4.py
"""
Write a function to convert a list of lists to a dictionary.
assert list_to_dict([["a", 1], ["b", 2], ["c", 3]]) == {"a": 1, "b": 2, "c": 3}
"""

def list_to_dict(lst):
    return dict(zip(*lst))

print(list_to_dict([["a", 1], ["b", 2], ["c", 3]]))
/python/list_to_dict_5.py
"""
Write a function to convert a list of lists to a dictionary.
assert list_to_dict([["a", 1], ["b", 2], ["c", 3]]) == {"a": 1, "b": 2, "c": 3}
"""

def list_to_dict(lst):
    return dict(zip(*lst))

print(list_to_dict([["a", 1], ["b", 2], ["c", 3]]))
/python/list_to_dict_6.py
"""
Write a function to convert a list of lists to a dictionary.
assert list_to_dict([["a", 1], ["b", 2], ["c", 3]]) == {"a": 1, "b": 2, "c": 3}
"""

def list_to_dict(lst):
    return dict(zip(*lst))

print(list_to_dict([["a", 1], ["b", 2], ["c", 3]]))
/python/list_to_dict_7.py
"""
Write a function to convert a list of lists to a dictionary.
assert list_to_dict([["a", 1], ["b", 2], ["c", 3]]) == {"a": 1, "b": 2, "c": 3}
"""

def list_to_dict(lst):
    return dict(zip(*lst))

print