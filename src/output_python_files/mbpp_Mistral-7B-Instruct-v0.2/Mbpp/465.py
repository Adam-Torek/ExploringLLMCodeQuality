"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""
def drop_empty(dictionary):
    """
    :param dictionary: A dictionary
    :return: A new dictionary without empty items
    """
    return {key: value for key, value in dictionary.items() if value is not None}

# Test
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}) == {'c1': 'Red', 'c2': 'Green'}</s>