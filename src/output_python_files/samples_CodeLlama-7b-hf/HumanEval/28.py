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
    """ Split string into a list of strings
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


def split_at(string: str, index: int) -> List[str]:
    """ Split string into a list of strings
    >>> split_at('', 0)
    ['']
    >>> split_at('abc', 0)
    ['', 'abc']
    >>> split_at('abc', 1)
    ['a', 'bc']
    >>> split_at('abc', 2)
    ['ab', 'c']
    >>> split_at('abc', 3)
    ['abc', '']
    >>> split_at('abc', 4)
    ['abc', '']
    """
    return string[:index], string[index:]


def split_at_last(string: str, delimiter: str) -> List[str]:
    """ Split string into a list of strings
    >>> split_at_last('', '')
    ['']
    >>> split_at_last('abc', '')
    ['abc']
    >>> split_at_last('abc', 'a')
    ['', 'bc']
    >>> split_at_last('abc', 'b')
    ['a', 'c']
    >>> split_at_last('abc', 'c')
    ['ab', '']
    >>> split_at_last('abc', 'd')
    ['abc']
    """
    index = string.rfind(delimiter)
    if index == -1:
        return [string]
    return split_at(string, index)


def split_at_last_char(string: str, delimiter: str) -> List[str]:
    """ Split string into a list of strings
    >>> split_at_last_char('', '')
    ['']
    >>> split_at_last_char('abc', '')
    ['abc']
    >>> split_at_last_char('abc', 'a')
    ['', 'bc']
    >>> split_at_last_char('abc', 'b')
    ['a', 'c']
    >>> split_at_last_char('abc', 'c')
    ['ab', '']
    >>> split_at_last_char('abc', 'd')
    ['abc']
    """
    index = string.rfind(delimiter)
    if index == -1:
        return [string]
    return split_at(string, index + 1)


def split_at_first(string: str, delimiter: str) -> List[str]:
    """ Split string into a list of strings
    >>> split_at_first('', '')
    ['']
    >>> split_at_first('abc', '')
    ['abc']
    >>> split_at_first('abc', 'a')
    ['a', 'bc']
    >>> split_at_first('abc', 'b')
    ['abc', '']
    >>> split_at_first('abc', 'c')
    ['ab', 'c']
    >>> split_at_first('abc', 'd')
    ['abc']
    """
    index = string.find(delimiter)
    if index == -1:
        return [string]
    return split_at(string, index)


def split_at_first_char(string: str, delimiter: str) -> List[str]:
    """ Split string into a list of strings
    >>> split_at_first_char('', '')
    ['']
    >>> split_at_first_char('abc', '')
    ['abc']