"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""

def list_to_float(list_of_lists):
    return [[float(x) for x in sublist] for sublist in list_of_lists]

print(list_to_float([["3", "4"], ["1", "26.45"], ["7.32", "8"], ["4", "8"]]))
/python/list_to_dict.py
"""
Write a function to convert a list of lists to a dictionary.
assert list_to_dict([["a", 1], ["b", 2], ["c", 3]]) == {"a": 1, "b": 2, "c": 3}
"""

def list_to_dict(list_of_lists):
    return {sublist[0]: sublist[1] for sublist in list_of_lists}

print(list_to_dict([["a", 1], ["b", 2], ["c", 3]]))
/python/list_to_string.py
"""
Write a function to convert a list of lists to a string.
assert list_to_string([["a", 1], ["b", 2], ["c", 3]]) == "a1b2c3"
"""

def list_to_string(list_of_lists):
    return "".join(["".join(sublist) for sublist in list_of_lists])

print(list_to_string([["a", 1], ["b", 2], ["c", 3]]))
/python/list_to_tuple.py
"""
Write a function to convert a list of lists to a tuple.
assert list_to_tuple([["a", 1], ["b", 2], ["c", 3]]) == (("a", 1), ("b", 2), ("c", 3))
"""

def list_to_tuple(list_of_lists):
    return tuple(tuple(sublist) for sublist in list_of_lists)

print(list_to_tuple([["a", 1], ["b", 2], ["c", 3]]))
/python/list_to_set.py
"""
Write a function to convert a list to a set.
assert list_to_set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
"""

def list_to_set(list_of_lists):
    return set(list_of_lists)

print(list_to_set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_to_list.py
"""
Write a function to convert a list of lists to a list.
assert list_to_list([["a", 1], ["b", 2], ["c", 3]]) == ["a", 1, "b", 2, "c", 3]
"""

def list_to_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

print(list_to_list([["a", 1], ["b", 2], ["c", 3]]))
/python/list_to_dict_of_lists.py
"""
Write a function to convert a list of lists to a dictionary of lists.
assert list_to_dict_of_lists([["a", 1], ["b", 2], ["c", 3]]) == {"a": [1], "b": [2], "c": [3]}
"""

def list_to_dict_of_lists(list_of_lists):
    return {sublist[0]: [sublist[1]] for sublist in list_of_lists}