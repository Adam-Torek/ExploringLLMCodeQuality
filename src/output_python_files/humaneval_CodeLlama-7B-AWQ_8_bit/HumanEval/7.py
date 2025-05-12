from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given length
    >>> filter_by_length([], 3)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 3)
    ['abc', 'cde']
    """
    return [s for s in strings if len(s) == length]


def filter_by_substring_and_length(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring and have given length
    >>> filter_by_substring_and_length([], 'a', 3)
    []
    >>> filter_by_substring_and_length(['abc', 'bacd', 'cde', 'array'], 'a', 3)
    ['abc', 'cde']
    """
    return [s for s in strings if substring in s and len(s) == length]


def filter_by_substring_or_length(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring or have given length
    >>> filter_by_substring_or_length([], 'a', 3)
    []
    >>> filter_by_substring_or_length(['abc', 'bacd', 'cde', 'array'], 'a', 3)
    ['abc', 'bacd', 'cde', 'array']
    """
    return [s for s in strings if substring in s or len(s) == length]


def filter_by_substring_and_length_or(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring and have given length
    >>> filter_by_substring_and_length_or([], 'a', 3)
    []
    >>> filter_by_substring_and_length_or(['abc', 'bacd', 'cde', 'array'], 'a', 3)
    ['abc', 'cde']
    """
    return [s for s in strings if substring in s and len(s) == length or substring in s or len(s) == length]


def filter_by_substring_and_length_and(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring and have given length
    >>> filter_by_substring_and_length_and([], 'a', 3)
    []
    >>> filter_by_substring_and_length_and(['abc', 'bacd', 'cde', 'array'], 'a', 3)
    ['abc', 'cde']
    """
    return [s for s in strings if substring in s and len(s) == length and substring in s and len(s) == length]


def filter_by_substring_and_length_or_and(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring and have given length
    >>> filter_by_substring_and_length_or_and([], 'a', 3)
    []
    >>> filter_by_substring_and_length_or_and(['abc', 'bacd', 'cde', 'array'], 'a', 3)
    ['abc', 'cde']
    """
    return [s for s in strings if substring in s and len(s) == length or substring in s and len(s) == length and substring in s and len(s) == length]


def filter_by_