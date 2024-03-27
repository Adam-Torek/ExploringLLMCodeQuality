from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split()
    numbers.sort()
    return ' '.join(numbers)


def sort_words(words: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted from smallest to largest
    >>> sort_words('three one five')
    'five one three'
    """
    words = words.split()
    words.sort()
    return ' '.join(words)


def sort_words_by_length(words: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted from shortest to longest
    >>> sort_words_by_length('three one five')
    'three one five'
    """
    words = words.split()
    words.sort(key=len)
    return ' '.join(words)


def sort_words_by_length_reverse(words: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted from longest to shortest
    >>> sort_words_by_length_reverse('three one five')
    'five one three'
    """
    words = words.split()
    words.sort(key=len, reverse=True)
    return ' '.join(words)


def sort_words_by_length_reverse_alt(words: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted from longest to shortest
    >>> sort_words_by_length_reverse_alt('three one five')
    'five one three'
    """
    words = words.split()
    words.sort(key=len, reverse=True)
    return ' '.join(words)


def sort_words_by_length_reverse_alt2(words: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted from longest to shortest
    >>> sort_words_by_length_reverse_alt2('three one five')
    'five one three'
    """
    words = words.split()
    words.sort(key=len, reverse=True)
    return ' '.join(words)


def sort_words_by_length_reverse_alt3(words: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted from longest to shortest
    >>> sort_words_by_length_reverse_alt3('three one five')
    'five one three'
    """
    words = words.split()
    words.sort(key=len, reverse=True)
    return ' '.join(words)


def sort_words_by_length_reverse_alt4(words: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted from longest to shortest
    >>> sort_words_by_length_reverse_alt4('three one five')
    'five one three'
    """
    words = words.split()
    words.sort(key=len, reverse=True)
    return ' '.join(words)


def sort_words_by_length_reverse_alt5(words: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted from longest to shortest
    >>> sort_words_by_length_reverse_alt5('three one five')
    'five one three'
    """
    words = words.split()
    words.sort(key=len, reverse=True)
    return ' '.join(words)


def sort_words_by_length_reverse_alt6(words: str) -> str:
    """ Input is a