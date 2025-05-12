from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
<file_sep>/python/tests/test_remove_duplicates.py
from python.remove_duplicates import remove_duplicates


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
<file_sep>/python/tests/test_reverse_string.py
from python.reverse_string import reverse_string


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
<file_sep>/python/tests/test_reverse_words.py
from python.reverse_words import reverse_words


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
<file_sep>/python/reverse_words.py
from typing import List


def reverse_words(sentence: str) -> str:
    """ Reverse the order of words in a sentence.
    >>> reverse_words("hello world")
    "world hello"
    """
<file_sep>/python/tests/test_reverse_string.py
from python.reverse_string import reverse_string


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
<file_sep>/python/tests/test_reverse_words.py
from python.reverse_words import reverse_words


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
<file_sep>/python/reverse_string.py
def reverse_string(string: str) -> str:
    """ Reverse a string.
    >>> reverse_string("hello")
    "olleh"
    """
<|endoftext|>