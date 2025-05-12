from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(len(string) + 1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    """
    return [string[i:] for i in range(len(string) + 1)]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('abc')
    ['a', 'b', 'c', 'ab', 'bc', 'abc']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_substrings_with_overlap(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    with overlap
    >>> all_substrings_with_overlap('abc')
    ['a', 'ab', 'b', 'bc', 'c', 'abc']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_substrings_with_overlap_2(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    with overlap
    >>> all_substrings_with_overlap_2('abc')
    ['a', 'ab', 'b', 'bc', 'c', 'abc']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i, len(string) + 1)]


def all_substrings_with_overlap_3(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    with overlap
    >>> all_substrings_with_overlap_3('abc')
    ['a', 'ab', 'b', 'bc', 'c', 'abc']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i, len(string))]


def all_substrings_with_overlap_4(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    with overlap
    >>> all_substrings_with_overlap_4('abc')
    ['a', 'ab', 'b', 'bc', 'c', 'abc']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i, len(string) + 1)]


def all_substrings_with_overlap_5(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    with overlap
    >>> all_substrings_with_overlap_5('abc')
    ['a', 'ab', 'b', 'bc', 'c', 'abc']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i, len(string))]


def all_substrings_with_overlap_6(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    with overlap
    >>> all_substrings_with_overlap_6('abc')
    ['a', 'ab', 'b', 'bc', 'c', 'abc']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i, len(string))]


def all_substrings_with_overlap_7(string: str) -> List[str]:
    """ Return list of all substrings