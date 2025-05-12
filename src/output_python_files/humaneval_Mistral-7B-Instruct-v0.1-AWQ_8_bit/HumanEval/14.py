from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(len(string) + 1):
        prefixes.append(string[:i])
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['a', 'ab', 'abc']
    """
    suffixes = []
    for i in range(len(string) + 1):
        suffixes.append(string[i:])
    return suffixes