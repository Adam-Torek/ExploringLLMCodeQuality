from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


def filter_float(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_float(['a', 3.14, 5])
    [3.14]
    >>> filter_float([1, 2, 3, 'abc', {}, []])
    []
    """
    return [value for value in values if isinstance(value, float)]


def filter_string(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_string(['a', 3.14, 5])
    []
    >>> filter_string(['1', '2', '3', 'abc', {}, []])
    ['1', '2', '3']
    """
    return [value for value in values if isinstance(value, str)]


def filter_dict(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dict(['a', 3.14, 5])
    []
    >>> filter_dict(['1', '2', '3', 'abc', {}, []])
    ['{}']
    """
    return [value for value in values if isinstance(value, dict)]


def filter_list(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for lists
    >>> filter_list(['a', 3.14, 5])
    []
    >>> filter_list(['1', '2', '3', 'abc', {}, []])
    ['[]']
    """
    return [value for value in values if isinstance(value, list)]


def filter_tuple(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuple(['a', 3.14, 5])
    []
    >>> filter_tuple(['1', '2', '3', 'abc', {}, []])
    []
    """
    return [value for value in values if isinstance(value, tuple)]


def filter_set(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for sets
    >>> filter_set(['a', 3.14, 5])
    []
    >>> filter_set(['1', '2', '3', 'abc', {}, []])
    []
    """
    return [value for value in values if isinstance(value, set)]


def filter_bool(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for booleans
    >>> filter_bool(['a', 3.14, 5])
    []
    >>> filter_bool(['1', '2', '3', 'abc', {}, []])
    []
    """
    return [value for value in values if isinstance(value, bool)]


def filter_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for None
    >>> filter_none(['a', 3.14, 5])
    []
    >>> filter_none(['1', '2', '3', 'abc', None, []])
    ['None']
    """
    return [value for value in values if value is None]


def filter_any(values: List[Any], filter_func: Any) -> List[Any]:
    """ Filter given list of any python values using any filter function
    >>> filter_any(['a', 3.14, 5], filter_integers)
    [5]
    >>> filter_any(['1', '2', '3', 'abc', {}, []], filter_string)
    ['1', '2', '3']
    """
    return [value for value in values