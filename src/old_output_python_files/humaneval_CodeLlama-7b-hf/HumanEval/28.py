from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


def split(string: str, delimiter: str) -> List[str]:
    """ Split string into list of strings
    >>> split('', '')
    []
    >>> split('abc', '')
    ['a', 'b', 'c']
    >>> split('abc', 'a')
    ['', 'bc']
    >>> split('abc', 'b')
    ['a', 'c']
    >>> split('abc', 'c')
    ['ab', '']
    >>> split('abc', 'd')
    ['abc']
    """
    return string.split(delimiter)


def split_by_spaces(string: str) -> List[str]:
    """ Split string into list of strings by spaces
    >>> split_by_spaces('')
    []
    >>> split_by_spaces('abc')
    ['abc']
    >>> split_by_spaces('a b c')
    ['a', 'b', 'c']
    >>> split_by_spaces('a  b  c')
    ['a', 'b', 'c']
    >>> split_by_spaces('a b c d')
    ['a', 'b', 'c', 'd']
    """
    return split(string, ' ')


def split_by_newlines(string: str) -> List[str]:
    """ Split string into list of strings by newlines
    >>> split_by_newlines('')
    []
    >>> split_by_newlines('abc')
    ['abc']
    >>> split_by_newlines('a\nb\nc')
    ['a', 'b', 'c']
    >>> split_by_newlines('a\n\nb\n\nc')
    ['a', '', 'b', '', 'c']
    >>> split_by_newlines('a\nb\nc\n')
    ['a', 'b', 'c', '']
    >>> split_by_newlines('a\nb\nc\nd')
    ['a', 'b', 'c', 'd']
    """
    return split(string, '\n')


def split_by_tabs(string: str) -> List[str]:
    """ Split string into list of strings by tabs
    >>> split_by_tabs('')
    []
    >>> split_by_tabs('abc')
    ['abc']
    >>> split_by_tabs('a\tb\tc')
    ['a', 'b', 'c']
    >>> split_by_tabs('a\t\tb\t\tc')
    ['a', '', 'b', '', 'c']
    >>> split_by_tabs('a\tb\tc\t')
    ['a', 'b', 'c', '']
    >>> split_by_tabs('a\tb\tc\td')
    ['a', 'b', 'c', 'd']
    """
    return split(string, '\t')


def split_by_commas(string: str) -> List[str]:
    """ Split string into list of strings by commas
    >>> split_by_commas('')
    []
    >>> split_by_commas('abc')
    ['abc']
    >>> split_by_commas('a,b,c')
    ['a', 'b', 'c']
    >>> split_by_commas('a,,b,,c')
    ['a', '', 'b', '', 'c']
    >>> split_by_commas('a,b,c,')
    ['a', 'b', 'c', '']
    >>> split_by_commas('a,b,c,d')
    ['a', 'b', 'c', 'd']
    """
    return split(string, ',')


def split_by_semicolons(string: str) -> List[str]:
    """ Split string into list of strings by semicolons
    >>> split_by_semicolons('')
    []
    >>> split_by_semicolons('abc')
    ['abc']
    >>> split_by_semicolons('a;