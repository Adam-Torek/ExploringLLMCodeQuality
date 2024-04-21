"""
Write a function to add a dictionary to the tuple. The output should be a tuple.
assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
"""

def add_dict_to_tuple(tup, dict):
    tup = tup + (dict,)
    return tup

assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})

"""
Write a function to remove the last element from a tuple. The output should be a tuple.
assert remove_last_element_from_tuple((4, 5, 6)) == (4, 5)
"""

def remove_last_element_from_tuple(tup):
    tup = tup[:-1]
    return tup

assert remove_last_element_from_tuple((4, 5, 6)) == (4, 5)

"""
Write a function to remove the first element from a tuple. The output should be a tuple.
assert remove_first_element_from_tuple((4, 5, 6)) == (5, 6)
"""

def remove_first_element_from_tuple(tup):
    tup = tup[1:]
    return tup

assert remove_first_element_from_tuple((4, 5, 6)) == (5, 6)

"""
Write a function to remove the first and last element from a tuple. The output should be a tuple.
assert remove_first_and_last_element_from_tuple((4, 5, 6)) == (5,)
"""

def remove_first_and_last_element_from_tuple(tup):
    tup = tup[1:-1]
    return tup

assert remove_first_and_last_element_from_tuple((4, 5, 6)) == (5,)

"""
Write a function to remove the first and last element from a tuple. The output should be a tuple.
assert remove_first_and_last_element_from_tuple((4, 5, 6)) == (5,)
"""

def remove_first_and_last_element_from_tuple(tup):
    tup = tup[1:-1]
    return tup

assert remove_first_and_last_element_from_tuple((4, 5, 6)) == (5,)

"""
Write a function to remove the first and last element from a tuple. The output should be a tuple.
assert remove_first_and_last_element_from_tuple((4, 5, 6)) == (5,)
"""

def remove_first_and_last_element_from_tuple(tup):
    tup = tup[1:-1]
    return tup

assert remove_first_and_last_element_from_tuple((4, 5, 6)) == (5,)

"""
Write a function to remove the first and last element from a tuple. The output should be a tuple.
assert remove_first_and_last_element_from_tuple((4, 5, 6)) == (5,)
"""

def remove_first_and_last_element_from_tuple(tup):
    tup = tup[1:-1]
    return tup

assert remove_first_and_last_element_from_tuple((4, 5, 6)) == (5,)

"""
Write a function to remove the first and last element from a tuple. The output should be a tuple.
assert remove_first_and_last_element_from_tuple((4, 5, 6)) == (5,)
"""

def remove_first_and_last_element_from_tuple(tup):
    tup = tup[1:-1]
    return tup

assert remove_first_and_last_element_from_tuple((4, 5, 6)) == (5,)

"""
Write a function to remove the first and last element from a tuple. The output should be a tuple.
assert remove_first_and_last_element_from_tuple((4, 5, 6)) ==