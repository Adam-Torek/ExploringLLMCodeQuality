"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""


def first_non_repeating_character(string):
    """
    >>> first_non_repeating_character("abcabc")
    None
    >>> first_non_repeating_character("abca")
    'a'
    >>> first_non_repeating_character("abcaa")
    'a'
    >>> first_non_repeating_character("abcaab")
    'b'
    >>> first_non_repeating_character("abcaabb")
    'b'
    >>> first_non_repeating_character("abcaabbb")
    'b'
    >>> first_non_repeating_character("abcaabbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    'b'
    >>> first_non_repeating_character("abcaabbb