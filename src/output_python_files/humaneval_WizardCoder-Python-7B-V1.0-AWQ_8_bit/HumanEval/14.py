from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'bc', 'abc']
    """
    return [string[i:] for i in range(len(string))]

def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c', 'c', 'c']
    """
    return all_prefixes(string) + all_suffixes(string)

def all_substrings_with_length(string: str, length: int) -> List[str]:
    """ Return list of all substrings of the given length
    >>> all_substrings_with_length('abc', 2)
    ['ab', 'bc']
    """
    return [string[i:i+length] for i in range(len(string) - length + 1)]

def all_substrings_with_length_between(string: str, min_length: int, max_length: int) -> List[str]:
    """ Return list of all substrings with length between min_length and max_length
    >>> all_substrings_with_length_between('abc', 1, 2)
    ['a', 'ab', 'bc', 'c']
    """
    return [string[i:i+length] for length in range(min_length, max_length + 1) for i in range(len(string) - length + 1)]

def all_substrings_with_length_greater_than(string: str, min_length: int) -> List[str]:
    """ Return list of all substrings with length greater than or equal to min_length
    >>> all_substrings_with_length_greater_than('abc', 2)
    ['ab', 'bc', 'c']
    """
    return [string[i:i+min_length] for i in range(len(string) - min_length + 1)]

def all_substrings_with_length_less_than(string: str, max_length: int) -> List[str]:
    """ Return list of all substrings with length less than or equal to max_length
    >>> all_substrings_with_length_less_than('abc', 2)
    ['a', 'ab', 'b']
    """
    return [string[i:i+max_length] for i in range(len(string)) for length in range(max_length)]

def all_substrings_with_length_between(string: str, min_length: int, max_length: int) -> List[str]:
    """ Return list of all substrings with length between min_length and max_length
    >>> all_substrings_with_length_between('abc', 1, 2)
    ['a', 'ab', 'bc']
    """
    return [string[i:i+length] for length in range(min_length, max_length + 1) for i in range(len(string) - length + 1)]

def all_substrings_with_length_equal_to(string: str, length: int) -> List[str]:
    """ Return list of all substrings with length equal to the given length
    >>> all_substrings_with_length_equal_to('abc', 2)
    ['ab', 'bc']
    """
    return [string[i:i+length] for i in range(len(string) - length + 1) if len(string[i:i+length]) == length]

def all_substrings_with_length_not_equal_to(string: str, length: int) -> List[str]:
    """ Return list of all substrings with length not equal