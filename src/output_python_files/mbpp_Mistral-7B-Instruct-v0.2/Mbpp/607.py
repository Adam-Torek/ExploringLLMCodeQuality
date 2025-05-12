"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""
import re

def find_literals(string: str, pattern: str) -> tuple:
    """
    Searches a string for a regex pattern and returns the matching substring, start index and end index.

    :param string: The string to search in.
    :param pattern: The regex pattern to search for.
    :return: A tuple containing the matching substring, start index and end index.
    """
    match = re.search(pattern, string)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return (None, -1, -1)