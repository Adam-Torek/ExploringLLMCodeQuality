"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""

def list_to_float(list_of_lists):
    return [tuple(map(float, sublist)) for sublist in list_of_lists]

print(list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]))
/python/list_to_dict.py
"""
Write a function to convert a list of lists to a dictionary.
assert list_to_dict([["a", 1], ["b", 2], ["c", 3]]) == {"a": 1, "b": 2, "c": 3}
"""

def list_to_dict(list_of_lists):
    return {key: value for key, value in list_of_lists}

print(list_to_dict([["a", 1], ["b", 2], ["c", 3]]))
/python/list_to_string.py
"""
Write a function to convert a list of strings to a single string.
assert list_to_string(["a", "b", "c"]) == "abc"
"""

def list_to_string(list_of_strings):
    return "".join(list_of_strings)

print(list_to_string(["a", "b", "c"]))
/python/list_to_tuple.py
"""
Write a function to convert a list of lists to a tuple of tuples.
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

def list_to_set(list_of_numbers):
    return set(list_of_numbers)

print(list_to_set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_to_list.py
"""
Write a function to convert a list of lists to a list of tuples.
assert list_to_list([["a", 1], ["b", 2], ["c", 3]]) == [("a", 1), ("b", 2), ("c", 3)]
"""

def list_to_list(list_of_lists):
    return [tuple(sublist) for sublist in list_of_lists]

print(list_to_list([["a", 1], ["b", 2], ["c", 3]]))
/python/list_to_string_with_join.py
"""
Write a function to convert a list of strings to a single string using join.
assert list_to_string_with_join(["a", "b", "c"]) == "abc"
"""

def list_to_string_with_join(list_of_strings):
    return "".join(list_of_strings)

print(list_to_string_with_join(["a", "b", "c"]))
/python/list_to_string_with_join_and_map.py
"""
Write a function to convert a list of strings to a single string using join and map.
assert list_to_string_with_join_and