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
    return [string[i:j] for i in range(len(string) + 1) for j in range(i + 1, len(string) + 1)]


def all_substrings_with_overlap(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    with overlap
    >>> all_substrings_with_overlap('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_substrings_with_overlap_and_duplicates(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    with overlap and duplicates
    >>> all_substrings_with_overlap_and_duplicates('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c', 'ab', 'bc', 'abc']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i, len(string) + 1)]


def all_substrings_with_overlap_and_duplicates_and_order(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    with overlap and duplicates and order
    >>> all_substrings_with_overlap_and_duplicates_and_order('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c', 'ab', 'bc', 'abc', 'c', 'bc', 'abc']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i, len(string) + 1)]


def all_substrings_with_overlap_and_duplicates_and_order_and_reversed(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    with overlap and duplicates and order and reversed
    >>> all_substrings_with_overlap_and_duplicates_and_order_and_reversed('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c', 'ab', 'bc', 'abc', 'c', 'bc', 'abc', 'c', 'bc', 'abc']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i, len(string) + 1)]


def all_substrings_with_overlap_and_duplicates_and_order_and_reversed_and_reversed(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    with overlap and duplicates and order and reversed and reversed
    >>> all_substrings_with_overlap_and_duplicates_and_order_and_reversed_and_reversed('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c', 'ab', 'bc', 'abc', 'c', 'bc',