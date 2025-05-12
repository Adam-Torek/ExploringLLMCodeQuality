"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""
def drop_empty(dictionary):
    """
    :param dictionary: A dictionary
    :return: A new dictionary with empty items removed
    """
    return {key: value for key, value in dictionary.items() if value is not None}

# Testing
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}) == {'c1': 'Red', 'c2': 'Green'}
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':''}) == {'c1': 'Red', 'c2': 'Green'}
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':0}) == {'c1': 'Red', 'c2': 'Green'}
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':[]}) == {'c1': 'Red', 'c2': 'Green'}
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':{}}) == {'c1': 'Red', 'c2': 'Green'}
assert drop_empty({}) == {}
assert drop_empty({'c1': None}) == {}
assert drop_empty({'c1': None, 'c2': None}) == {}
assert drop_empty({'c1': None, 'c2': None, 'c3': None}) == {}
assert drop_empty({'c1': None, 'c2': None, 'c3': None, 'c4': 'Green'}) == {'c4': 'Green'}