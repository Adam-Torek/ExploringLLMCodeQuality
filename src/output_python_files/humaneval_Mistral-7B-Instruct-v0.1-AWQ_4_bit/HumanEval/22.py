from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    >>> filter_floats([1, 2, 3, 'abc', {}, []])
    []
    """
    return [value for value in values if isinstance(value, float)]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    []
    >>> filter_strings(['1', '2', '3', 'abc', {}, []])
    ['1', '2', '3']
    """
    return [value for value in values if isinstance(value, str)]


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dicts(['a', 3.14, 5])
    []
    >>> filter_dicts(['1', '2', '3', 'abc', {}, []])
    ['{}']
    """
    return [value for value in values if isinstance(value, dict)]


def filter_lists(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5])
    []
    >>> filter_lists(['1', '2', '3', 'abc', {}, []])
    ['{}']
    """
    return [value for value in values if isinstance(value, list)]