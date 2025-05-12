from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


def longest_with_default(strings: List[str], default: str) -> str:
    """ Out of list of strings, return the longest one. Return the default value in case the input
    list is empty.
    >>> longest_with_default([], 'default')
    'default'
    >>> longest_with_default(['a', 'b', 'c'], 'default')
    'a'
    >>> longest_with_default(['a', 'bb', 'ccc'], 'default')
    'ccc'
    """
    if not strings:
        return default
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


def longest_with_default_2(strings: List[str], default: str) -> str:
    """ Out of list of strings, return the longest one. Return the default value in case the input
    list is empty.
    >>> longest_with_default_2([], 'default')
    'default'
    >>> longest_with_default_2(['a', 'b', 'c'], 'default')
    'a'
    >>> longest_with_default_2(['a', 'bb', 'ccc'], 'default')
    'ccc'
    """
    if not strings:
        return default
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


def longest_with_default_3(strings: List[str], default: str) -> str:
    """ Out of list of strings, return the longest one. Return the default value in case the input
    list is empty.
    >>> longest_with_default_3([], 'default')
    'default'
    >>> longest_with_default_3(['a', 'b', 'c'], 'default')
    'a'
    >>> longest_with_default_3(['a', 'bb', 'ccc'], 'default')
    'ccc'
    """
    if not strings:
        return default
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


def longest_with_default_4(strings: List[str], default: str) -> str:
    """ Out of list of strings, return the longest one. Return the default value in case the input
    list is empty.
    >>> longest_with_default_4([], 'default')
    'default'
    >>> longest_with_default_4(['a', 'b', 'c'], 'default')
    'a'
    >>> longest_with_default_4(['a', 'bb', 'ccc'], 'default')
    'ccc'
    """
    if not strings:
        return default
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


def longest_with_default_5(strings: List[str], default: str) -> str:
    """ Out of list of strings, return the longest one. Return the default value in case the input
    list is empty.
    >>> longest_with_default_5([], 'default')
    'default'
    >>> longest_with_default_5(['a', 'b', 'c'], 'default')
    'a'
    >>> longest_with_default_5(['a', 'bb', 'ccc'], 'default')
    'ccc'