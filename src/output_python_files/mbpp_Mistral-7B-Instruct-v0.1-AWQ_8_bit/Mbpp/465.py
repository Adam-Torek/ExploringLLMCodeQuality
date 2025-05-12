"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""

def drop_empty(dictionary):
    """
    This function takes a dictionary as an input and returns a new dictionary with all the empty values removed.
    """
    new_dictionary = {}
    for key in dictionary:
        if dictionary[key] != None:
            new_dictionary[key] = dictionary[key]
    return new_dictionary

# Test the function
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}