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
    >>> filter_by_length([], 1)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 3)
    ['abc', 'bacd']
    """
    return [s for s in strings if len(s) == length]


def filter_by_vowel_count(strings: List[str], count: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given number of vowels
    >>> filter_by_vowel_count([], 1)
    []
    >>> filter_by_vowel_count(['abc', 'bacd', 'cde', 'array'], 3)
    ['abc', 'bacd']
    """
    return [s for s in strings if s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') == count]


def filter_by_consonant_count(strings: List[str], count: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given number of consonants
    >>> filter_by_consonant_count([], 1)
    []
    >>> filter_by_consonant_count(['abc', 'bacd', 'cde', 'array'], 3)
    ['abc', 'bacd']
    """
    return [s for s in strings if s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') == count]


def filter_by_even_length(strings: List[str]) -> List[str]:
    """ Filter an input list of strings only for ones that have even length
    >>> filter_by_even_length([])
    []
    >>> filter_by_even_length(['abc', 'bacd', 'cde', 'array'])
    ['abc', 'cde']
    """
    return [s for s in strings if len(s) % 2 == 0]


def filter_by_odd_length(strings: List[str]) -> List[str]:
    """ Filter an input list of strings only for ones that have odd length
    >>> filter_by_odd_length([])
    []
    >>> filter_by_odd_length(['abc', 'bacd', 'cde', 'array'])
    ['bacd']
    """
    return [s for s in strings if len(s) % 2 == 1]


def filter_by_vowel_count_and_length(strings: List[str], count: int, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given number of vowels and length
    >>> filter_by_vowel_count_and_length([], 1, 1)
    []
    >>> filter_by_vowel_count_and_length(['abc', 'bacd', 'cde', 'array'], 3, 3)
    ['abc', 'bacd']
    """
    return [s for s in strings if s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') == count and len(s) == length]


def filter_by_consonant_count_and_length(strings: List[str], count: int, length: int) -> List[str]:
    """ Filter an input list of