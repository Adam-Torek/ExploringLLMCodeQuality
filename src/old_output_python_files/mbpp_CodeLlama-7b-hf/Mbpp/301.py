"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""


def dict_depth(d):
    """
    :param d: dictionary
    :return: depth of the dictionary
    """
    if not isinstance(d, dict):
        return 0
    else:
        return 1 + max(dict_depth(v) for v in d.values())


if __name__ == '__main__':
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict