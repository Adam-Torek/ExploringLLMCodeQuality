"""
Write a function to add a dictionary to the tuple. The output should be a tuple.
assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
"""

def add_dict_to_tuple(tuple, dict):
    return tuple + (dict,)

print(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ))

"""
Write a function to add a list to the tuple. The output should be a tuple.
assert add_list_to_tuple((4, 5, 6), [1, 2, 3] ) == (4, 5, 6, [1, 2, 3])
"""

def add_list_to_tuple(tuple, list):
    return tuple + (list,)

print(add_list_to_tuple((4, 5, 6), [1, 2, 3] ))

"""
Write a function to add a set to the tuple. The output should be a tuple.
assert add_set_to_tuple((4, 5, 6), {1, 2, 3} ) == (4, 5, 6, {1, 2, 3})
"""

def add_set_to_tuple(tuple, set):
    return tuple + (set,)

print(add_set_to_tuple((4, 5, 6), {1, 2, 3} ))

"""
Write a function to add a string to the tuple. The output should be a tuple.
assert add_string_to_tuple((4, 5, 6), "MSAM" ) == (4, 5, 6, 'MSAM')
"""

def add_string_to_tuple(tuple, string):
    return tuple + (string,)

print(add_string_to_tuple((4, 5, 6), "MSAM" ))

"""
Write a function to add a float to the tuple. The output should be a tuple.
assert add_float_to_tuple((4, 5, 6), 1.234 ) == (4, 5, 6, 1.234)
"""

def add_float_to_tuple(tuple, float):
    return tuple + (float,)

print(add_float_to_tuple((4, 5, 6), 1.234 ))

"""
Write a function to add an integer to the tuple. The output should be a tuple.
assert add_integer_to_tuple((4, 5, 6), 1 ) == (4, 5, 6, 1)
"""

def add_integer_to_tuple(tuple, integer):
    return tuple + (integer,)

print(add_integer_to_tuple((4, 5, 6), 1 ))

"""
Write a function to add a boolean to the tuple. The output should be a tuple.
assert add_boolean_to_tuple((4, 5, 6), True ) == (4, 5, 6, True)
"""

def add_boolean_to_tuple(tuple, boolean):
    return tuple + (boolean,)

print(add_boolean_to_tuple((4, 5, 6), True ))

"""
Write a function to add a None to the tuple. The output should be a tuple.
assert add_none_to_tuple((4, 5, 6), None ) == (4, 5, 6, None)
"""

def add_none_to_tuple(tuple, none):
    return tuple + (none,)

print(add_none_to_tuple((4, 5, 6), None ))

"""
Write a function to add a function to