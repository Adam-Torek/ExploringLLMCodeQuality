"""
Write a function to add a dictionary to the tuple. The output should be a tuple.
assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
"""

def add_dict_to_tuple(tup, dict_to_add):
    return tup + (dict_to_add,)

print(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} )) # Output: (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})

# or

def add_dict_to_tuple(tup, dict_to_add):
    return tup + (dict_to_add,)

print(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} )) # Output: (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})