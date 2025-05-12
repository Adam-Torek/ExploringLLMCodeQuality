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
    return max(strings, key=len)


def longest_prefix(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest common prefix. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest_prefix([])

    >>> longest_prefix(['a', 'b', 'c'])
    None
    >>> longest_prefix(['a', 'ab', 'abc'])
    'a'
    """
    if not strings:
        return None
    return ''.join(max(strings, key=lambda x: x[:len(x) - 1]))


def longest_suffix(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest common suffix. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest_suffix([])

    >>> longest_suffix(['a', 'b', 'c'])
    None
    >>> longest_suffix(['a', 'ab', 'abc'])
    'c'
    """
    if not strings:
        return None
    return ''.join(max(strings, key=lambda x: x[len(x) - 1:]))


def longest_common_subsequence(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest common subsequence. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest_common_subsequence([])

    >>> longest_common_subsequence(['a', 'b', 'c'])
    None
    >>> longest_common_subsequence(['a', 'ab', 'abc'])
    'a'
    """
    if not strings:
        return None
    return ''.join(max(strings, key=lambda x: x[1:len(x) - 1]))


def longest_common_substring(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest common substring. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest_common_substring([])

    >>> longest_common_substring(['a', 'b', 'c'])
    None
    >>> longest_common_substring(['a', 'ab', 'abc'])
    'a'
    """
    if not strings:
        return None
    return ''.join(max(strings, key=lambda x: x[1:len(x) - 1]))


def longest_common_subarray(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest common subarray. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest_common_subarray([])

    >>> longest_common_subarray(['a', 'b', 'c'])
    None
    >>> longest_common_subarray(['a', 'ab', 'abc'])
    'a'
    """
    if not strings:
        return None
    return ''.join(max(strings, key=lambda x: x[1:len(x) - 1]))


def longest_common_substring_with_replacement(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest common substring with replacement. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest_common_substring_with_replacement([])

    >>> longest_common_substring_with_replacement(['a', 'b', 'c'])
    None
    >>> longest