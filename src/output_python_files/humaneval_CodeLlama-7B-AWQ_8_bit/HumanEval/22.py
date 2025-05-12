from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    """
    return [value for value in values if isinstance(value, str)]


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    >>> filter_floats([1, 2, 3, 'abc', {}, []])
    []
    """
    return [value for value in values if isinstance(value, float)]


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dicts(['a', 3.14, 5])
    []
    >>> filter_dicts([1, 2, 3, 'abc', {}, []])
    [{'__class__': 'dict', '__module__': 'builtins'}, {}]
    """
    return [value for value in values if isinstance(value, dict)]


def filter_lists(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5])
    []
    >>> filter_lists([1, 2, 3, 'abc', {}, []])
    [[1, 2, 3], []]
    """
    return [value for value in values if isinstance(value, list)]


def filter_tuples(values: List[Any]) -> List[tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples(['a', 3.14, 5])
    []
    >>> filter_tuples([1, 2, 3, 'abc', {}, []])
    [(1, 2, 3), ()]
    """
    return [value for value in values if isinstance(value, tuple)]


def filter_sets(values: List[Any]) -> List[set]:
    """ Filter given list of any python values only for sets
    >>> filter_sets(['a', 3.14, 5])
    []
    >>> filter_sets([1, 2, 3, 'abc', {}, []])
    [{1, 2, 3}, set()]
    """
    return [value for value in values if isinstance(value, set)]


def filter_functions(values: List[Any]) -> List[callable]:
    """ Filter given list of any python values only for functions
    >>> filter_functions(['a', 3.14, 5])
    []
    >>> filter_functions([1, 2, 3, 'abc', {}, []])
    [<built-in function abs>, <built-in function all>, <built-in function any>, <built-in function ascii>, <built-in function bin>, <built-in function bool>, <built-in function breakpoint>, <built-in function bytearray>, <built-in function bytes>, <built-in function callable>, <built-in function chr>, <built-in function classmethod>, <built-in function compile>, <built-in function complex>, <built-in function delattr>, <built-in function dict>, <built-in function dir>, <built-in function divmod>, <built-in function enumerate>, <built-in function eval>, <built-in function exec>, <built-in function filter>, <built-in function float>, <built-in function