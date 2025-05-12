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
    >>> first_non_repeating_character("abcaaa")
    'a'
    >>> first_non_repeating_character("abcaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_character("abcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    'a'
    >>> first_non_repeating_