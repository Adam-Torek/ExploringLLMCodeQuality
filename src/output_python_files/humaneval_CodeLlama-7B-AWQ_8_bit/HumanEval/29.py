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
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 3)
    ['abc', 'bcd', 'cde']
    """
    return [s for s in strings if len(s) == length]


def filter_by_vowel_count(strings: List[str], vowel_count: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a given number of vowels.
    >>> filter_by_vowel_count([], 1)
    []
    >>> filter_by_vowel_count(['abc', 'bcd', 'cde', 'array'], 1)
    ['abc', 'array']
    >>> filter_by_vowel_count(['abc', 'bcd', 'cde', 'array'], 3)
    ['abc', 'cde', 'array']
    """
    return [s for s in strings if s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') == vowel_count]


def filter_by_consonant_count(strings: List[str], consonant_count: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a given number of consonants.
    >>> filter_by_consonant_count([], 1)
    []
    >>> filter_by_consonant_count(['abc', 'bcd', 'cde', 'array'], 1)
    ['abc', 'array']
    >>> filter_by_consonant_count(['abc', 'bcd', 'cde', 'array'], 3)
    ['abc', 'bcd', 'array']
    """
    return [s for s in strings if s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') + s.count('y') == consonant_count]


def filter_by_even_length(strings: List[str]) -> List[str]:
    """ Filter an input list of strings only for ones that have an even length.
    >>> filter_by_even_length([])
    []
    >>> filter_by_even_length(['abc', 'bcd', 'cde', 'array'])
    ['abc', 'cde']
    """
    return [s for s in strings if len(s) %