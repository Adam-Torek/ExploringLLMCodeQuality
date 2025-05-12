"""
Write a function to check whether all dictionaries in a list are empty or not.
assert empty_dit([{},{},{}])==True
"""
def empty_dit(list_of_dit):
    for dit in list_of_dit:
        if dit:
            return False
    return True

"""
Write a function to check whether all the items of a list is a string or not.
assert all_string([1,2,3])==False
assert all_string(['a','b','c'])==True
"""
def all_string(list_of_items):
    for item in list_of_items:
        if not isinstance(item, str):
            return False
    return True

"""
Write a function to check whether all the items of a list is a number or not.
assert all_number([1,2,3])==True
assert all_number(['a','b','c'])==False
"""
def all_number(list_of_items):
    for item in list_of_items:
        if not isinstance(item, int):
            return False
    return True

"""
Write a function to check whether all the items of a list is a list or not.
assert all_list([1,2,3])==False
assert all_list([[],[],[]])==True
"""
def all_list(list_of_items):
    for item in list_of_items:
        if not isinstance(item, list):
            return False
    return True

"""
Write a function to check whether all the items of a list is a tuple or not.
assert all_tuple([1,2,3])==False
assert all_tuple([(1,2),(3,4),(5,6)])==True
"""
def all_tuple(list_of_items):
    for item in list_of_items:
        if not isinstance(item, tuple):
            return False
    return True

"""
Write a function to check whether all the items of a list is a set or not.
assert all_set([1,2,3])==False
assert all_set([set([1]),set([2]),set([3])])==True
"""
def all_set(list_of_items):
    for item in list_of_items:
        if not isinstance(item, set):
            return False
    return True

"""
Write a function to check whether all the items of a list is a frozenset or not.
assert all_frozenset([1,2,3])==False
assert all_frozenset([frozenset([1]),frozenset([2]),frozenset([3])])==True
"""
def all_frozenset(list_of_items):
    for item in list_of_items:
        if not isinstance(item, frozenset):
            return False
    return True

"""
Write a function to check whether all the items of a list is a dict or not.
assert all_dict([1,2,3])==False
assert all_dict([{},{},{}])==True
"""
def all_dict(list_of_items):
    for item in list_of_items:
        if not isinstance(item, dict):
            return False
    return True

"""
Write a function to check whether all the items of a list is a bool or not.
assert all_bool([1,2,3])==False
assert all_bool([True,True,True])==True
"""
def all_bool(list_of_items):
    for item in list_of_items:
        if not isinstance(item, bool):
            return False
    return True

"""
Write a function to check whether all the items of a list is a float or not.
assert all_float([1,2,3])==False
assert all_float([1.1,2.2,3.3])==True
"""
def all_float(list_of_items):
    for item in list_of_items:
        if not isinstance(item, float):
            return False
    return True

"""
Write a function to check whether all the items of a list is a complex or not.
assert all_complex([1,2,3])==False
assert all_complex([1+2j,3+4j,5+