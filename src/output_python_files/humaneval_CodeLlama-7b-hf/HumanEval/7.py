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
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if len(string) == length]


def filter_by_vowel_count(strings: List[str], vowel_count: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given number of vowels
    >>> filter_by_vowel_count([], 1)
    []
    >>> filter_by_vowel_count(['abc', 'bacd', 'cde', 'array'], 3)
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u') == vowel_count]


def filter_by_consonant_count(strings: List[str], consonant_count: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given number of consonants
    >>> filter_by_consonant_count([], 1)
    []
    >>> filter_by_consonant_count(['abc', 'bacd', 'cde', 'array'], 3)
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u') == consonant_count]


def filter_by_even_length(strings: List[str]) -> List[str]:
    """ Filter an input list of strings only for ones that have even length
    >>> filter_by_even_length([])
    []
    >>> filter_by_even_length(['abc', 'bacd', 'cde', 'array'])
    ['abc', 'bacd', 'cde']
    """
    return [string for string in strings if len(string) % 2 == 0]


def filter_by_odd_length(strings: List[str]) -> List[str]:
    """ Filter an input list of strings only for ones that have odd length
    >>> filter_by_odd_length([])
    []
    >>> filter_by_odd_length(['abc', 'bacd', 'cde', 'array'])
    ['bacd', 'array']
    """
    return [string for string in strings if len(string) % 2 == 1]


def filter_by_vowel_position(strings: List[str], position: int) -> List[str]:
    """ Filter an input list of strings only for ones that have vowel in given position
    >>> filter_by_vowel_position([], 1)
    []
    >>> filter_by_vowel_position(['abc', 'bacd', 'cde', 'array'], 3)
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if string[position] in 'aeiou']


def filter_by_consonant_position(strings: List[str], position: int) -> List[str]:
    """ Filter an input list of strings only for ones that have consonant in given position
    >>> filter_by_consonant_position([], 1)
    []