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
    return 1 + max(dict_depth(v) for v in d.values())


if __name__ == '__main__':
    print(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {}}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {}}}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {}}}}}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {}}}}}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {}}}}}}}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {}}}}}}}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {}}}}}}}}}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {}}}}}}}}}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {}}}}}}}}}}}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {}}}}}}}}}}}}}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {'q': {}}}}}}}}}}}}}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {'q': {'r': {}}}}}}}}}}}}}}}}}}}}))
    print(dict_depth({'a': 1, 'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {'q': {'r': {'s': {}}}}