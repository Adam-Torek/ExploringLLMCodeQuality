from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have length between min_length and max_length
    >>> filter_by_length([], 1, 2)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 1, 2)
    ['abc', 'bacd']
    """
    return [s for s in strings if min_length <= len(s) <= max_length]


def filter_by_length_and_substring(strings: List[str], min_length: int, max_length: int, substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that have length between min_length and max_length and contain given substring
    >>> filter_by_length_and_substring([], 1, 2, 'a')
    []
    >>> filter_by_length_and_substring(['abc', 'bacd', 'cde', 'array'], 1, 2, 'a')
    ['abc', 'bacd']
    """
    return [s for s in strings if min_length <= len(s) <= max_length and substring in s]


def filter_by_length_or_substring(strings: List[str], min_length: int, max_length: int, substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that have length between min_length and max_length or contain given substring
    >>> filter_by_length_or_substring([], 1, 2, 'a')
    []
    >>> filter_by_length_or_substring(['abc', 'bacd', 'cde', 'array'], 1, 2, 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if min_length <= len(s) <= max_length or substring in s]


def filter_by_length_and_substring_or(strings: List[str], min_length: int, max_length: int, substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that have length between min_length and max_length and contain given substring or contain substring
    >>> filter_by_length_and_substring_or([], 1, 2, 'a')
    []
    >>> filter_by_length_and_substring_or(['abc', 'bacd', 'cde', 'array'], 1, 2, 'a')
    ['abc', 'bacd']
    """
    return [s for s in strings if min_length <= len(s) <= max_length and (substring in s or substring in s)]


def filter_by_length_or_substring_and(strings: List[str], min_length: int, max_length: int, substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that have length between min_length and max_length or contain given substring and contain substring
    >>> filter_by_length_or_substring_and([], 1, 2, 'a')
    []
    >>> filter_by_length_or_substring_and(['abc', 'bacd', 'cde', 'array'], 1, 2, 'a')
    ['abc', 'bacd']
    """
    return [s for s in strings if min_length <= len(s) <= max_length or (substring in s and substring in s)]


def filter_by_length_and_substring_and(strings: List[str], min_length: int, max_length: int, substring: str) -> List[str]:
    """ Filter an input list of strings only for ones