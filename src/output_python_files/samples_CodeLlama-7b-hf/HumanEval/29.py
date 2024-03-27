from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.endswith(suffix)]


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain a given substring.
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'bcd', 'cde', 'array']
    """
    return [s for s in strings if substring in s]


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a given length.
    >>> filter_by_length([], 1)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 1)
    ['a', 'b', 'c', 'd', 'e', 'r', 'a', 'y']
    """
    return [s for s in strings if len(s) == length]


def filter_by_length_range(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a given length range.
    >>> filter_by_length_range([], 1, 2)
    []
    >>> filter_by_length_range(['abc', 'bcd', 'cde', 'array'], 1, 2)
    ['a', 'b', 'c', 'd', 'e', 'r', 'a', 'y']
    """
    return [s for s in strings if min_length <= len(s) <= max_length]


def filter_by_length_gt(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a given length greater than.
    >>> filter_by_length_gt([], 1)
    []
    >>> filter_by_length_gt(['abc', 'bcd', 'cde', 'array'], 1)
    ['bcd', 'cde', 'array']
    """
    return [s for s in strings if len(s) > length]


def filter_by_length_lt(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a given length less than.
    >>> filter_by_length_lt([], 1)
    []
    >>> filter_by_length_lt(['abc', 'bcd', 'cde', 'array'], 1)
    ['abc']
    """
    return [s for s in strings if len(s) < length]


def filter_by_length_gte(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a given length greater than or equal to.
    >>> filter_by_length_gte([], 1)
    []
    >>> filter_by_length_gte(['abc', 'bcd', 'cde', 'array'], 1)
    ['abc', 'bcd', 'cde', 'array']
    """
    return [s for s in strings if len(s) >= length]


def filter