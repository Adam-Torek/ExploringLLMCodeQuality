"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""


def dict_depth(d):
    """
    >>> dict_depth({'a':1, 'b': {'c': {'d': {}}}})
    4
    """
    if isinstance(d, dict):
        return 1 + max(dict_depth(v) for v in d.values())
    else:
        return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()