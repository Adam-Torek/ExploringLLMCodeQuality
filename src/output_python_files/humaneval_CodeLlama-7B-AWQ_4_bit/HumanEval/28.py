from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


def concatenate_with_delimiter(strings: List[str], delimiter: str) -> str:
    """ Concatenate list of strings into a single string with a delimiter
    >>> concatenate_with_delimiter([], '')
    ''
    >>> concatenate_with_delimiter(['a', 'b', 'c'], ' ')
    'a b c'
    """
    return delimiter.join(strings)


def concatenate_with_delimiter_and_capitalize(strings: List[str], delimiter: str) -> str:
    """ Concatenate list of strings into a single string with a delimiter and capitalize first letter of each word
    >>> concatenate_with_delimiter_and_capitalize([], '')
    ''
    >>> concatenate_with_delimiter_and_capitalize(['a', 'b', 'c'], ' ')
    'A B C'
    """
    return delimiter.join(map(lambda x: x.capitalize(), strings))


def concatenate_with_delimiter_and_capitalize_first_letter(strings: List[str], delimiter: str) -> str:
    """ Concatenate list of strings into a single string with a delimiter and capitalize first letter of each word
    >>> concatenate_with_delimiter_and_capitalize_first_letter([], '')
    ''
    >>> concatenate_with_delimiter_and_capitalize_first_letter(['a', 'b', 'c'], ' ')
    'A b c'
    """
    return delimiter.join(map(lambda x: x.capitalize(), strings))


def concatenate_with_delimiter_and_capitalize_last_letter(strings: List[str], delimiter: str) -> str:
    """ Concatenate list of strings into a single string with a delimiter and capitalize last letter of each word
    >>> concatenate_with_delimiter_and_capitalize_last_letter([], '')
    ''
    >>> concatenate_with_delimiter_and_capitalize_last_letter(['a', 'b', 'c'], ' ')
    'a b C'
    """
    return delimiter.join(map(lambda x: x.capitalize(), strings))


def concatenate_with_delimiter_and_capitalize_first_and_last_letter(strings: List[str], delimiter: str) -> str:
    """ Concatenate list of strings into a single string with a delimiter and capitalize first and last letter of each word
    >>> concatenate_with_delimiter_and_capitalize_first_and_last_letter([], '')
    ''
    >>> concatenate_with_delimiter_and_capitalize_first_and_last_letter(['a', 'b', 'c'], ' ')
    'A B C'
    """
    return delimiter.join(map(lambda x: x.capitalize(), strings))


def concatenate_with_delimiter_and_capitalize_first_and_last_letter_and_remove_duplicate_delimiter(
        strings: List[str], delimiter: str) -> str:
    """ Concatenate list of strings into a single string with a delimiter and capitalize first and last letter of each word
    and remove duplicate delimiter
    >>> concatenate_with_delimiter_and_capitalize_first_and_last_letter_and_remove_duplicate_delimiter([], '')
    ''
    >>> concatenate_with_delimiter_and_capitalize_first_and_last_letter_and_remove_duplicate_delimiter(['a', 'b', 'c'], ' ')
    'A B C'
    """
    return delimiter.join(map(lambda x: x.capitalize(), strings))


def