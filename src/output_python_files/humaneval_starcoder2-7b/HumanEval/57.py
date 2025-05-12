def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

def is_palindrome(s: str):
    """Return True if string is a palindrome.
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('hello')
    False
    >>> is_palindrome('hannah')
    True
    """

def is_anagram(s1: str, s2: str):
    """Return True if strings are anagrams.
    >>> is_anagram('hello', 'olleh')
    True
    >>> is_anagram('hello', 'olleh')
    True
    >>> is_anagram('hello', 'olleh')
    True
    """

def is_palindrome_anagram(s: str):
    """Return True if string is a palindrome and an anagram of itself.
    >>> is_palindrome_anagram('hello')
    False
    >>> is_palindrome_anagram('hannah')
    True
    >>> is_palindrome_anagram('racecar')
    True
    """

def is_palindrome_anagram_case_insensitive(s: str):
    """Return True if string is a palindrome and an anagram of itself,
    ignoring case.
    >>> is_palindrome_anagram_case_insensitive('hello')
    False
    >>> is_palindrome_anagram_case_insensitive('hannah')
    True
    >>> is_palindrome_anagram_case_insensitive('racecar')
    True
    """

def is_palindrome_anagram_case_insensitive_no_spaces(s: str):
    """Return True if string is a palindrome and an anagram of itself,
    ignoring case and spaces.
    >>> is_palindrome_anagram_case_insensitive_no_spaces('hello')
    False
    >>> is_palindrome_anagram_case_insensitive_no_spaces('hannah')
    True
    >>> is_palindrome_anagram_case_insensitive_no_spaces('racecar')
    True
    """

def is_palindrome_anagram_case_insensitive_no_spaces_no_punctuation(s: str):
    """Return True if string is a palindrome and an anagram of itself,
    ignoring case, spaces, and punctuation.
    >>> is_palindrome_anagram_case_insensitive_no_spaces_no_punctuation('hello')
    False
    >>> is_palindrome_anagram_case_insensitive_no_spaces_no_punctuation('hannah')
    True
    >>> is_palindrome_anagram_case_insensitive_no_spaces_no_punctuation('racecar')
    True
    """

def is_palindrome_anagram_case_insensitive_no_spaces_no_punctuation_no_numbers(s: str):
    """Return True if string is a palindrome and an anagram of itself,
    ignoring case, spaces, punctuation, and numbers.
    >>> is_palindrome_anagram_case_insensitive_no_spaces_no_punctuation_no_numbers('hello')
    False
    >>> is_palindrome_anagram_case_insensitive_no_spaces_no_punctuation_no_numbers('hannah')
    True
    >>> is_palindrome_anagram_case_insensitive_no_spaces_no_punctuation_no_numbers('racecar')
    True
    """

def is_palindrome_anagram_case_insensitive_no_spaces_no_punctuation_no_numbers_no_symbols(s: str):
    """Return True if string is a palindrome and an anagram of itself,
    ignoring case, spaces, punctuation, numbers, and symbols.
    >>> is_palindrome_anagram_case_insensitive_no_spaces_no_punctuation_no_numbers_no_symbols('hello')
    False
    >>> is_palindrome_anagram_case_insensitive_no_spaces_no_punctuation_no_numbers_no_symbols('hannah')
    True
    >>> is_palindrome_anagram_case_insensitive_