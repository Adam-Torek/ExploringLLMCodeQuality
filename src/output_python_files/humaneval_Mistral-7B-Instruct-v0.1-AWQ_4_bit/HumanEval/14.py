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


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings of the input string
    >>> all_substrings('abc')
    ['a', 'ab', 'abc', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
    """
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            substrings.append(string[i:j])
    return substrings


def all_substrings_with_repeated_chars(string: str) -> List[str]:
    """ Return list of all substrings of the input string with repeated characters
    >>> all_substrings_with_repeated_chars('aab')
    ['a', 'a', 'a', 'ab', 'ba', 'b', 'ab', 'ba', 'bb']
    """
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            substrings.append(string[i:j])
    return substrings


def all_substrings_without_repeated_chars(string: str) -> List[str]:
    """ Return list of all substrings of the input string without repeated characters
    >>> all_substrings_without_repeated_chars('aab')
    ['a', 'b']
    """
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            substrings.append(string[i:j])
    return [substring for substring in substrings if len(substring) > 1 and substring[0] != substring[-1]]


def all_substrings_with_repeated_chars_and_length_greater_than_one(string: str) -> List[str]:
    """ Return list of all substrings of the input string with repeated characters and length greater than one
    >>> all_substrings_with_repeated_chars_and_length_greater_than_one('aab')
    ['a', 'a', 'a', 'ab', 'ba', 'b', 'ab', 'ba', 'bb']
    """
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            substrings.append(string[i:j])
    return [substring for substring in substrings if len(substring) > 1 and substring[0] != substring[-1]]


def all_substrings_without_repeated_chars_and_length_greater_than_one(string: str) -> List[str]:
    """ Return list of all substrings of the input string without repeated characters and length greater than one
    >>> all_substrings_without_repeated_chars_and_length_greater_than_one('aab')
    []
    """
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            substrings.append(string[i:j])
    return [substring for substring in substrings if len(substring) > 1 and substring[0