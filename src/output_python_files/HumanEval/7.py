from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given length
    >>> filter_by_length([], 1)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 3)
    ['abc', 'bacd', 'cde']
    """
    return [string for string in strings if len(string) == length]


def filter_by_length_range(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given length
    >>> filter_by_length_range([], 1, 3)
    []
    >>> filter_by_length_range(['abc', 'bacd', 'cde', 'array'], 3, 5)
    ['abc', 'bacd', 'cde']
    """
    return [string for string in strings if min_length <= len(string) <= max_length]


def filter_by_vowel_count(strings: List[str], vowel_count: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given number of vowels
    >>> filter_by_vowel_count([], 1)
    []
    >>> filter_by_vowel_count(['abc', 'bacd', 'cde', 'array'], 3)
    ['abc', 'bacd', 'cde']
    """
    return [string for string in strings if string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u') == vowel_count]


def filter_by_vowel_count_range(strings: List[str], min_vowel_count: int, max_vowel_count: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given number of vowels
    >>> filter_by_vowel_count_range([], 1, 3)
    []
    >>> filter_by_vowel_count_range(['abc', 'bacd', 'cde', 'array'], 3, 5)
    ['abc', 'bacd', 'cde']
    """
    return [string for string in strings if string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u') >= min_vowel_count and string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u') <= max_vowel_count]


def filter_by_consonant_count(strings: List[str], consonant_count: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given number of consonants
    >>> filter_by_consonant_count([], 1)
    []
    >>> filter_by_consonant_count(['abc', 'bacd', 'cde', 'array'], 3)
    ['abc', 'bacd', 'cde']
    """
    return [string for string in strings if string.count('b') + string.count('c') + string.count('d') + string.count('f') + string.count('g') + string.count('h') + string.count('j') + string.count('k') + string.count('l') + string.count('m') + string.count('n') + string.count('p') + string.count('q') + string.count('r') + string.count('s') + string.count('t') + string.count('v