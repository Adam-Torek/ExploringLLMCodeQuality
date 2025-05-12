def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))

def unique_dict(d: dict):
    """Return a new dictionary with unique keys
    >>> unique_dict({'a': 1, 'b': 2, 'a': 3, 'c': 4})
    {'a': 1, 'b': 2, 'c': 4}
    """
    return {k: v for k, v in d.items() if k not in d.keys()}

def unique_list(l: list):
    """Return a new list with unique elements
    >>> unique_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return list(set(l))

def unique_tuple(t: tuple):
    """Return a new tuple with unique elements
    >>> unique_tuple((5, 3, 5, 2, 3, 3, 9, 0, 123))
    (0, 2, 3, 5, 9, 123)
    """
    return tuple(set(t))

def unique_set(s: set):
    """Return a new set with unique elements
    >>> unique_set({'a': 1, 'b': 2, 'a': 3, 'c': 4})
    {'a': 1, 'b': 2, 'c': 4}
    """
    return {k: v for k, v in s.items() if k not in s.keys()}

def unique_string(s: str):
    """Return a new string with unique characters
    >>> unique_string('hello world')
    'hldw'
    """
    return ''.join(sorted(set(s)))

def unique_bytes(b: bytes):
    """Return a new bytes object with unique bytes
    >>> unique_bytes(b'hello world')
    b'hldw'
    """
    return bytes(sorted(set(b)))